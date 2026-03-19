# -*- coding: utf-8 -*-
"""
Werewolf Game Utility Functions - Unit Tests
Using Python's built-in unittest module
"""

import unittest
import random
from werewolf.utils import (
    get_role_distribution,
    assign_roles,
    check_win_condition,
    get_alive_players,
    get_player_by_id,
    format_player_list,
    ROLE_ABILITIES
)


# =============================================================================
# Test 1: get_role_distribution(player_count)
# =============================================================================

class TestGetRoleDistribution(unittest.TestCase):
    """Test role distribution for different player counts."""
    
    def test_5_players(self):
        """Test distribution for 5 players."""
        result = get_role_distribution(5)
        self.assertEqual(result['werewolf'], 1)
        self.assertEqual(result['villager'], 2)
        self.assertEqual(result['seer'], 1)
        self.assertEqual(result['hunter'], 1)
        self.assertEqual(sum(result.values()), 5)
    
    def test_7_players(self):
        """Test distribution for 7 players."""
        result = get_role_distribution(7)
        self.assertEqual(result['werewolf'], 2)
        self.assertEqual(result['villager'], 3)
        self.assertEqual(result['seer'], 1)
        self.assertEqual(result['hunter'], 1)
        self.assertEqual(sum(result.values()), 7)
    
    def test_10_players(self):
        """Test distribution for 10 players."""
        result = get_role_distribution(10)
        self.assertEqual(result['werewolf'], 2)
        self.assertEqual(result['villager'], 4)
        self.assertEqual(result['seer'], 1)
        self.assertEqual(result['hunter'], 1)
        self.assertEqual(result['witch'], 1)
        self.assertEqual(result['guard'], 1)
        self.assertEqual(sum(result.values()), 10)
    
    def test_12_players(self):
        """Test distribution for 12 players."""
        result = get_role_distribution(12)
        self.assertEqual(result['werewolf'], 3)
        self.assertEqual(result['villager'], 5)
        self.assertEqual(result['seer'], 1)
        self.assertEqual(result['hunter'], 1)
        self.assertEqual(result['witch'], 1)
        self.assertEqual(result['guard'], 1)
        self.assertEqual(result['cupid'], 1)
        self.assertEqual(sum(result.values()), 13)  # 13 roles for 12 players (gets adjusted)
    
    def test_15_players_scaling(self):
        """Test distribution scales for 15 players (uses 12 config + scaling)."""
        result = get_role_distribution(15)
        # 15 players should use 12 config with extra werewolves/villagers
        # (15-12)//4 = 0 extra, so should be same as 12
        self.assertGreaterEqual(result['werewolf'], 3)
        self.assertGreaterEqual(result['villager'], 5)
        self.assertGreaterEqual(sum(result.values()), 12)
    
    def test_returns_copy_not_reference(self):
        """Test that function returns a copy, not the original dict."""
        result1 = get_role_distribution(5)
        result2 = get_role_distribution(5)
        result1['werewolf'] = 999
        self.assertEqual(result2['werewolf'], 1)  # Should be unchanged


# =============================================================================
# Test 2: assign_roles(player_count, player_names)
# =============================================================================

class TestAssignRoles(unittest.TestCase):
    """Test role assignment functionality."""
    
    def test_valid_assignment_5_players(self):
        """Test valid assignment with 5 players."""
        names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
        result = assign_roles(5, names)
        
        self.assertEqual(len(result), 5)
        for i, player in enumerate(result):
            self.assertEqual(player['player_id'], i + 1)
            self.assertEqual(player['player_name'], names[i])
            self.assertIn('role', player)
            self.assertIn('team', player)
            self.assertTrue(player['alive'])
            self.assertFalse(player['abilities_used'])
    
    def test_valid_assignment_10_players(self):
        """Test valid assignment with 10 players."""
        names = ['Player{}'.format(i) for i in range(10)]
        result = assign_roles(10, names)
        
        self.assertEqual(len(result), 10)
        roles_assigned = [p['role'] for p in result]
        # Should have all expected roles
        self.assertGreaterEqual(roles_assigned.count('werewolf'), 2)
        self.assertIn('seer', roles_assigned)
    
    def test_mismatch_player_count_raises_error(self):
        """Test that mismatched player count raises ValueError."""
        names = ['Alice', 'Bob', 'Charlie']
        with self.assertRaises(ValueError) as context:
            assign_roles(5, names)
        self.assertIn("Expected 5 players, got 3", str(context.exception))
    
    def test_empty_player_list(self):
        """Test assignment with empty player list (edge case: 0 players)."""
        # This is an edge case - 0 players with empty list doesn't raise error
        # but returns empty list
        result = assign_roles(0, [])
        self.assertEqual(len(result), 0)
    
    def test_all_players_have_valid_teams(self):
        """Test that all assigned roles have valid teams."""
        names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
        result = assign_roles(5, names)
        
        valid_teams = ['good', 'evil', 'neutral']
        for player in result:
            self.assertIn(player['team'], valid_teams)
            # Verify team matches role definition
            self.assertEqual(player['team'], ROLE_ABILITIES[player['role']]['team'])
    
    def test_roles_are_shuffled(self):
        """Test that roles are randomized (not in fixed order)."""
        names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
        # Run multiple times to check randomness
        results = [assign_roles(5, names) for _ in range(5)]
        role_sequences = [tuple(p['role'] for p in r) for r in results]
        # Not all sequences should be identical (probabilistic)
        self.assertGreater(len(set(role_sequences)), 1)


# =============================================================================
# Test 3: check_win_condition(players)
# =============================================================================

class TestCheckWinCondition(unittest.TestCase):
    """Test win condition detection."""
    
    def test_good_wins_all_evil_dead(self):
        """Test good team wins when all evil are eliminated."""
        players = [
            {'player_id': 1, 'team': 'good', 'alive': True},
            {'player_id': 2, 'team': 'good', 'alive': True},
            {'player_id': 3, 'team': 'evil', 'alive': False},
        ]
        result = check_win_condition(players)
        self.assertEqual(result, 'good')
    
    def test_evil_wins_equal_numbers(self):
        """Test evil wins when they equal good in numbers."""
        players = [
            {'player_id': 1, 'team': 'good', 'alive': True},
            {'player_id': 2, 'team': 'good', 'alive': True},
            {'player_id': 3, 'team': 'evil', 'alive': True},
            {'player_id': 4, 'team': 'evil', 'alive': True},
        ]
        result = check_win_condition(players)
        self.assertEqual(result, 'evil')
    
    def test_evil_wins_more_evil_than_good(self):
        """Test evil wins when they outnumber good."""
        players = [
            {'player_id': 1, 'team': 'good', 'alive': True},
            {'player_id': 2, 'team': 'evil', 'alive': True},
            {'player_id': 3, 'team': 'evil', 'alive': True},
        ]
        result = check_win_condition(players)
        self.assertEqual(result, 'evil')
    
    def test_game_ongoing(self):
        """Test game continues when no win condition met."""
        players = [
            {'player_id': 1, 'team': 'good', 'alive': True},
            {'player_id': 2, 'team': 'good', 'alive': True},
            {'player_id': 3, 'team': 'good', 'alive': True},
            {'player_id': 4, 'team': 'evil', 'alive': True},
        ]
        result = check_win_condition(players)
        self.assertIsNone(result)
    
    def test_all_dead_returns_good(self):
        """Test when all players are dead - edge case."""
        players = [
            {'player_id': 1, 'team': 'good', 'alive': False},
            {'player_id': 2, 'team': 'evil', 'alive': False},
        ]
        result = check_win_condition(players)
        # No alive evil, so good wins (edge case)
        self.assertEqual(result, 'good')
    
    def test_only_evil_alive(self):
        """Test when only evil players are alive."""
        players = [
            {'player_id': 1, 'team': 'good', 'alive': False},
            {'player_id': 2, 'team': 'evil', 'alive': True},
            {'player_id': 3, 'team': 'evil', 'alive': True},
        ]
        result = check_win_condition(players)
        self.assertEqual(result, 'evil')
    
    def test_neutral_team_handling(self):
        """Test that neutral team members are counted as good."""
        players = [
            {'player_id': 1, 'team': 'good', 'alive': True},
            {'player_id': 2, 'team': 'neutral', 'alive': True},  # Cupid
            {'player_id': 3, 'team': 'evil', 'alive': False},
        ]
        result = check_win_condition(players)
        # Neutral is not evil, so good wins
        self.assertEqual(result, 'good')


# =============================================================================
# Test 4: get_alive_players(players, role)
# =============================================================================

class TestGetAlivePlayers(unittest.TestCase):
    """Test alive player filtering."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.players = [
            {'player_id': 1, 'player_name': 'Alice', 'role': 'werewolf', 'team': 'evil', 'alive': True},
            {'player_id': 2, 'player_name': 'Bob', 'role': 'villager', 'team': 'good', 'alive': True},
            {'player_id': 3, 'player_name': 'Charlie', 'role': 'seer', 'team': 'good', 'alive': False},
            {'player_id': 4, 'player_name': 'Diana', 'role': 'werewolf', 'team': 'evil', 'alive': True},
            {'player_id': 5, 'player_name': 'Eve', 'role': 'hunter', 'team': 'good', 'alive': True},
        ]
    
    def test_get_all_alive(self):
        """Test getting all alive players without role filter."""
        result = get_alive_players(self.players)
        self.assertEqual(len(result), 4)
        self.assertTrue(all(p['alive'] for p in result))
        names = [p['player_name'] for p in result]
        self.assertNotIn('Charlie', names)  # Charlie is dead
    
    def test_filter_by_role(self):
        """Test filtering alive players by specific role."""
        result = get_alive_players(self.players, role='werewolf')
        self.assertEqual(len(result), 2)
        self.assertTrue(all(p['role'] == 'werewolf' for p in result))
        names = [p['player_name'] for p in result]
        self.assertIn('Alice', names)
        self.assertIn('Diana', names)
    
    def test_filter_by_role_no_matches(self):
        """Test filtering by role with no matches."""
        result = get_alive_players(self.players, role='witch')
        self.assertEqual(len(result), 0)
    
    def test_all_dead(self):
        """Test when all players are dead."""
        all_dead = [
            {'player_id': 1, 'role': 'werewolf', 'alive': False},
            {'player_id': 2, 'role': 'villager', 'alive': False},
        ]
        result = get_alive_players(all_dead)
        self.assertEqual(len(result), 0)
    
    def test_all_alive(self):
        """Test when all players are alive."""
        all_alive = [
            {'player_id': 1, 'role': 'werewolf', 'alive': True},
            {'player_id': 2, 'role': 'villager', 'alive': True},
        ]
        result = get_alive_players(all_alive)
        self.assertEqual(len(result), 2)


# =============================================================================
# Test 5: get_player_by_id(players, player_id)
# =============================================================================

class TestGetPlayerById(unittest.TestCase):
    """Test player lookup by ID."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.players = [
            {'player_id': 1, 'player_name': 'Alice', 'role': 'werewolf'},
            {'player_id': 2, 'player_name': 'Bob', 'role': 'villager'},
            {'player_id': 3, 'player_name': 'Charlie', 'role': 'seer'},
        ]
    
    def test_find_existing_player(self):
        """Test finding an existing player."""
        result = get_player_by_id(self.players, 2)
        self.assertIsNotNone(result)
        self.assertEqual(result['player_name'], 'Bob')
        self.assertEqual(result['player_id'], 2)
    
    def test_find_first_player(self):
        """Test finding the first player."""
        result = get_player_by_id(self.players, 1)
        self.assertIsNotNone(result)
        self.assertEqual(result['player_name'], 'Alice')
    
    def test_find_last_player(self):
        """Test finding the last player."""
        result = get_player_by_id(self.players, 3)
        self.assertIsNotNone(result)
        self.assertEqual(result['player_name'], 'Charlie')
    
    def test_player_not_found(self):
        """Test when player ID doesn't exist."""
        result = get_player_by_id(self.players, 999)
        self.assertIsNone(result)
    
    def test_empty_player_list(self):
        """Test with empty player list."""
        result = get_player_by_id([], 1)
        self.assertIsNone(result)
    
    def test_zero_player_id(self):
        """Test with player ID of 0 (edge case)."""
        result = get_player_by_id(self.players, 0)
        self.assertIsNone(result)
    
    def test_negative_player_id(self):
        """Test with negative player ID."""
        result = get_player_by_id(self.players, -1)
        self.assertIsNone(result)


# =============================================================================
# Test 6: format_player_list(players, show_roles)
# =============================================================================

class TestFormatPlayerList(unittest.TestCase):
    """Test player list formatting."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.players = [
            {'player_id': 1, 'player_name': 'Alice', 'role': 'werewolf', 'alive': True},
            {'player_id': 2, 'player_name': 'Bob', 'role': 'villager', 'alive': True},
            {'player_id': 3, 'player_name': 'Charlie', 'role': 'seer', 'alive': False},
        ]
    
    def test_format_without_roles(self):
        """Test formatting without showing roles."""
        result = format_player_list(self.players, show_roles=False)
        lines = result.split('\n')
        self.assertEqual(len(lines), 3)
        self.assertIn('✅ Alice (#1)', lines[0])
        self.assertIn('✅ Bob (#2)', lines[1])
        self.assertIn('☠️ Charlie (#3)', lines[2])
        # Should not contain role descriptions
        self.assertNotIn('Werewolf', lines[0])
    
    def test_format_with_roles(self):
        """Test formatting with roles shown."""
        result = format_player_list(self.players, show_roles=True)
        lines = result.split('\n')
        self.assertEqual(len(lines), 3)
        self.assertIn('✅ Alice (#1)', lines[0])
        self.assertIn('🐺', lines[0])  # Werewolf emoji
        self.assertIn('☠️ Charlie (#3)', lines[2])
    
    def test_format_empty_list(self):
        """Test formatting empty player list."""
        result = format_player_list([], show_roles=False)
        self.assertEqual(result, '')
    
    def test_format_single_player(self):
        """Test formatting single player."""
        single = [{'player_id': 1, 'player_name': 'Solo', 'role': 'werewolf', 'alive': True}]
        result = format_player_list(single, show_roles=False)
        self.assertIn('✅ Solo (#1)', result)
    
    def test_status_icons_correct(self):
        """Test that alive/dead icons are correct."""
        mixed = [
            {'player_id': 1, 'player_name': 'Alive', 'role': 'villager', 'alive': True},
            {'player_id': 2, 'player_name': 'Dead', 'role': 'villager', 'alive': False},
        ]
        result = format_player_list(mixed, show_roles=False)
        self.assertIn('✅ Alive', result)
        self.assertIn('☠️ Dead', result)


# =============================================================================
# Run tests
# =============================================================================

if __name__ == '__main__':
    unittest.main(verbosity=2)
