# -*- coding: utf-8 -*-
"""
Werewolf Game Utility Functions
Helper functions for game logic
"""

import random
from typing import List, Dict, Optional


# Role definitions with their counts for different player sizes
ROLE_COUNTS = {
    # 5 players
    5: {
        'werewolf': 1,
        'villager': 2,
        'seer': 1,
        'hunter': 1
    },
    # 6-7 players
    7: {
        'werewolf': 2,
        'villager': 3,
        'seer': 1,
        'hunter': 1
    },
    # 8-10 players
    10: {
        'werewolf': 2,
        'villager': 4,
        'seer': 1,
        'hunter': 1,
        'witch': 1,
        'guard': 1
    },
    # 11+ players
    12: {
        'werewolf': 3,
        'villager': 5,
        'seer': 1,
        'hunter': 1,
        'witch': 1,
        'guard': 1,
        'cupid': 1
    }
}

# Role abilities and descriptions
ROLE_ABILITIES = {
    'werewolf': {
        'team': 'evil',
        'ability': 'Kill a player each night',
        'description': '🐺 Werewolf - Hunt villagers under cover of darkness'
    },
    'villager': {
        'team': 'good',
        'ability': 'No special ability',
        'description': '👨‍🌾 Villager - Find the werewolves through discussion'
    },
    'seer': {
        'team': 'good',
        'ability': 'Check one player\'s role each night',
        'description': '🔮 Seer - Reveal the truth'
    },
    'hunter': {
        'team': 'good',
        'ability': 'Take one player with you when you die',
        'description': '🏹 Hunter - Never die alone'
    },
    'witch': {
        'team': 'good',
        'ability': 'One heal potion, one poison potion',
        'description': '🧙 Witch - Master of potions'
    },
    'guard': {
        'team': 'good',
        'ability': 'Protect one player each night',
        'description': '🛡️ Guard - Shield the innocent'
    },
    'cupid': {
        'team': 'neutral',
        'ability': 'Link two players as lovers',
        'description': '💕 Cupid - Create eternal bonds'
    }
}


def get_role_distribution(player_count: int) -> Dict[str, int]:
    """
    Get the appropriate role distribution for the given player count.
    
    Args:
        player_count: Number of players in the game
        
    Returns:
        Dictionary mapping role names to their counts
    """
    # Find the closest matching configuration
    available_sizes = sorted(ROLE_COUNTS.keys())
    
    for size in available_sizes:
        if player_count <= size:
            return ROLE_COUNTS[size].copy()
    
    # For very large games, scale up werewolves
    base_config = ROLE_COUNTS[12].copy()
    extra_werewolves = (player_count - 12) // 4
    base_config['werewolf'] += extra_werewolves
    base_config['villager'] += extra_werewolves
    return base_config


def assign_roles(player_count: int, player_names: List[str]) -> List[Dict]:
    """
    Randomly assign roles to players.
    
    Args:
        player_count: Total number of players
        player_names: List of player names
        
    Returns:
        List of dictionaries with player info and assigned roles
    """
    if len(player_names) != player_count:
        raise ValueError(f"Expected {player_count} players, got {len(player_names)}")
    
    role_distribution = get_role_distribution(player_count)
    
    # Create role pool
    role_pool = []
    for role, count in role_distribution.items():
        role_pool.extend([role] * count)
    
    # Adjust if we have more/fewer roles than players
    while len(role_pool) < player_count:
        role_pool.append('villager')
    role_pool = role_pool[:player_count]
    
    # Shuffle roles
    random.shuffle(role_pool)
    
    # Assign roles to players
    assignments = []
    for i, name in enumerate(player_names):
        assignments.append({
            'player_id': i + 1,
            'player_name': name,
            'role': role_pool[i],
            'team': ROLE_ABILITIES[role_pool[i]]['team'],
            'alive': True,
            'abilities_used': False
        })
    
    return assignments


def check_win_condition(players: List[Dict]) -> Optional[str]:
    """
    Check if the game has reached a win condition.
    
    Args:
        players: List of player dictionaries
        
    Returns:
        'good' if good team wins, 'evil' if evil team wins, None if game continues
    """
    alive_good = 0
    alive_evil = 0
    
    for player in players:
        if not player['alive']:
            continue
            
        if player['team'] == 'evil':
            alive_evil += 1
        else:
            alive_good += 1
    
    # Evil wins if they equal or outnumber good
    if alive_evil >= alive_good and alive_evil > 0:
        return 'evil'
    
    # Good wins if all evil are eliminated
    if alive_evil == 0:
        return 'good'
    
    return None


def get_alive_players(players: List[Dict], role: Optional[str] = None) -> List[Dict]:
    """
    Get list of alive players, optionally filtered by role.
    
    Args:
        players: List of player dictionaries
        role: Optional role filter
        
    Returns:
        List of alive players matching criteria
    """
    alive = [p for p in players if p['alive']]
    if role:
        return [p for p in alive if p['role'] == role]
    return alive


def get_player_by_id(players: List[Dict], player_id: int) -> Optional[Dict]:
    """
    Find a player by their ID.
    
    Args:
        players: List of player dictionaries
        player_id: The player's ID
        
    Returns:
        Player dictionary or None if not found
    """
    for player in players:
        if player['player_id'] == player_id:
            return player
    return None


def format_player_list(players: List[Dict], show_roles: bool = False) -> str:
    """
    Format a player list for display.
    
    Args:
        players: List of player dictionaries
        show_roles: Whether to show player roles
        
    Returns:
        Formatted string representation
    """
    lines = []
    for player in players:
        status = '☠️' if not player['alive'] else '✅'
        role_info = f" - {ROLE_ABILITIES[player['role']]['description']}" if show_roles else ''
        lines.append(f"{status} {player['player_name']} (#{player['player_id']}){role_info}")
    return '\n'.join(lines)


# Unit tests can be written for these functions
if __name__ == '__main__':
    # Quick demo
    print("=== Werewolf Utility Demo ===\n")
    
    test_players = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    assignments = assign_roles(5, test_players)
    
    print("Role Assignments:")
    print(format_player_list(assignments, show_roles=True))
    
    print("\nWin Condition Check:", check_win_condition(assignments))
    
    print("\nAlive Players:")
    print(format_player_list(get_alive_players(assignments)))
