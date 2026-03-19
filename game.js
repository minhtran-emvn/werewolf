/**
 * Werewolf Game Logic
 * Handles game state, roles, and player actions
 */

class WerewolfGame {
    constructor() {
        this.multiplayer = new MultiplayerWerewolf();
        this.players = [];
        this.myPlayerId = null;
        this.myRole = null;
        this.gameState = 'lobby';
        this.phase = null;
        this.nightCount = 0;
        this.dayCount = 0;
        this.selectedPlayer = null;
        this.actionsReceived = {};
        
        // Role configurations
        this.ROLES = {
            werewolf: { icon: '🐺', name: 'Ma Sói', team: 'evil', count: 0 },
            villager: { icon: '👨‍🌾', name: 'Dân Làng', team: 'good', count: 0 },
            seer: { icon: '🔮', name: 'Tiên Tri', team: 'good', count: 1 },
            hunter: { icon: '🏹', name: 'Thợ Săn', team: 'good', count: 1 },
            witch: { icon: '🧙', name: 'Phù Thủy', team: 'good', count: 1 },
            guard: { icon: '🛡️', name: 'Bảo Vệ', team: 'good', count: 1 },
            cupid: { icon: '💕', name: 'Thần Tình Yêu', team: 'neutral', count: 0 }
        };

        this.setupMultiplayerHandlers();
    }

    /**
     * Setup multiplayer event handlers
     */
    setupMultiplayerHandlers() {
        // Handle player updates
        this.multiplayer.on('PLAYER_UPDATE', (data) => {
            this.players = data.players;
            this.updatePlayerList();
            this.updatePlayerCount();
        });

        // Handle game state updates
        this.multiplayer.on('GAME_STATE_UPDATE', (data) => {
            this.gameState = data.gameState;
            this.phase = data.phase;
            this.nightCount = data.nightCount || 0;
            this.dayCount = data.dayCount || 0;
            this.updateGameUI();
        });

        // Handle role assignment
        this.multiplayer.on('ROLE_ASSIGNMENT', (data) => {
            if (data.playerId === this.myPlayerId) {
                this.myRole = data.role;
                this.showMyRole(data.role);
            }
        });

        // Handle chat messages
        this.multiplayer.on('CHAT_MESSAGE', (data) => {
            this.addChatMessage(data.playerName, data.message, data.timestamp);
        });

        // Handle night actions (host only)
        this.multiplayer.on('NIGHT_ACTION', (data) => {
            this.handleNightAction(data);
        });

        // Handle votes (host only)
        this.multiplayer.on('VOTE', (data) => {
            this.handleVote(data);
        });
    }

    /**
     * Create a new room
     */
    async createRoom() {
        const name = document.getElementById('host-name').value || 'Host';
        
        try {
            const result = await this.multiplayer.initialize(true);
            this.myPlayerId = result.roomId;
            
            document.getElementById('lobby-section').classList.add('hidden');
            document.getElementById('room-section').classList.remove('hidden');
            document.getElementById('room-code-display').textContent = result.roomId;
            document.getElementById('host-controls').classList.remove('hidden');
            document.getElementById('waiting-message').classList.add('hidden');
            
            this.updatePlayerList();
            this.showNotification('✅ Tạo phòng thành công! Chia sẻ mã phòng với bạn bè.');
        } catch (error) {
            console.error('Failed to create room:', error);
            this.showNotification('❌ Không thể tạo phòng: ' + error.message);
        }
    }

    /**
     * Join an existing room
     */
    async joinRoom() {
        const roomCode = document.getElementById('room-code-input').value.trim();
        const name = document.getElementById('player-name').value || 'Player';
        
        if (!roomCode) {
            this.showNotification('❌ Vui lòng nhập mã phòng!');
            return;
        }

        try {
            await this.multiplayer.initialize(false);
            await this.multiplayer.joinRoom(roomCode, name);
            this.myPlayerId = this.multiplayer.peerId;
            
            document.getElementById('lobby-section').classList.add('hidden');
            document.getElementById('room-section').classList.remove('hidden');
            document.getElementById('room-code-display').textContent = roomCode;
            document.getElementById('host-controls').classList.add('hidden');
            
            this.updatePlayerList();
            this.showNotification('✅ Vào phòng thành công!');
        } catch (error) {
            console.error('Failed to join room:', error);
            this.showNotification('❌ Không thể vào phòng: ' + error.message);
        }
    }

    /**
     * Update player list UI
     */
    updatePlayerList() {
        const playerList = document.getElementById('player-list');
        const players = this.multiplayer.players;
        
        playerList.innerHTML = players.map((player, index) => `
            <div class="player-item ${player.isHost ? 'host' : ''}">
                <div class="player-status">
                    <span class="online"></span>
                    <span>${player.name} ${player.isHost ? '👑' : ''}</span>
                </div>
                <span style="color: #666;">#${index + 1}</span>
            </div>
        `).join('');
    }

    /**
     * Update player count
     */
    updatePlayerCount() {
        const count = this.multiplayer.players.length;
        document.getElementById('player-count').textContent = count;
        document.getElementById('start-game-btn').disabled = count < 5;
        
        if (this.multiplayer.isHost) {
            document.getElementById('room-status').textContent = 
                count >= 5 ? '✅ Sẵn sàng bắt đầu!' : `⏳ Cần thêm ${5 - count} người chơi`;
        }
    }

    /**
     * Copy room code to clipboard
     */
    copyRoomCode() {
        const code = document.getElementById('room-code-display').textContent;
        navigator.clipboard.writeText(code).then(() => {
            this.showNotification('📋 Đã sao chép mã phòng!');
        });
    }

    /**
     * Start the game (host only)
     */
    startGame() {
        if (!this.multiplayer.isHost) return;
        
        const playerCount = this.multiplayer.players.length;
        const roles = this.generateRoles(playerCount);
        
        // Start game for all players
        this.multiplayer.startGame(roles);
        
        // Assign my role locally
        const myPlayerIndex = this.multiplayer.players.findIndex(p => p.id === this.myPlayerId);
        this.myRole = roles[myPlayerIndex];
        this.showMyRole(this.myRole);
        
        // Update UI
        document.getElementById('room-section').classList.add('hidden');
        document.getElementById('game-section').classList.remove('hidden');
        
        this.gameState = 'playing';
        this.phase = 'night';
        this.nightCount = 1;
        
        this.updateGameUI();
        this.addGameLog('🌙 Đêm 1 bắt đầu!');
    }

    /**
     * Generate role distribution
     */
    generateRoles(playerCount) {
        let roles = [];
        
        if (playerCount <= 5) {
            roles = ['werewolf', 'villager', 'villager', 'seer', 'hunter'];
        } else if (playerCount <= 7) {
            roles = ['werewolf', 'werewolf', 'villager', 'villager', 'villager', 'seer', 'hunter'];
        } else if (playerCount <= 10) {
            roles = ['werewolf', 'werewolf', 'villager', 'villager', 'villager', 'villager', 
                     'seer', 'hunter', 'witch', 'guard'];
        } else {
            roles = ['werewolf', 'werewolf', 'werewolf', 'villager', 'villager', 'villager',
                     'villager', 'villager', 'seer', 'hunter', 'witch', 'guard', 'cupid'];
        }
        
        // Fill remaining with villagers
        while (roles.length < playerCount) {
            roles.push('villager');
        }
        
        // Shuffle roles
        for (let i = roles.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [roles[i], roles[j]] = [roles[j], roles[i]];
        }
        
        return roles;
    }

    /**
     * Show my role to player
     */
    showMyRole(role) {
        const roleData = this.ROLES[role];
        document.getElementById('my-role').textContent = roleData.icon;
        document.getElementById('my-role-name').textContent = roleData.name;
        document.getElementById('my-role-ability').textContent = 
            this.getRoleAbility(role);
    }

    /**
     * Get role ability description
     */
    getRoleAbility(role) {
        const abilities = {
            werewolf: 'Giết một người mỗi đêm',
            villager: 'Không có khả năng đặc biệt',
            seer: 'Xem vai trò của một người mỗi đêm',
            hunter: 'Kéo theo một người khi chết',
            witch: 'Một thuốc giải, một thuốc độc',
            guard: 'Bảo vệ một người mỗi đêm',
            cupid: 'Chọn hai người làm đôi uyên ương'
        };
        return abilities[role] || '';
    }

    /**
     * Update game UI based on phase
     */
    updateGameUI() {
        const phaseDisplay = document.getElementById('phase-display');
        const nightNumber = document.getElementById('night-number');
        const phaseAction = document.getElementById('phase-action');
        
        if (this.phase === 'night') {
            phaseDisplay.className = 'phase-indicator night';
            phaseDisplay.innerHTML = `
                <div>🌙 Đêm ${this.nightCount}</div>
                <div id="phase-action">${this.getNightActionText()}</div>
            `;
            this.setupNightActions();
        } else if (this.phase === 'day') {
            phaseDisplay.className = 'phase-indicator day';
            phaseDisplay.innerHTML = `
                <div>☀️ Ngày ${this.dayCount}</div>
                <div id="phase-action">Thảo luận và bỏ phiếu</div>
            `;
            this.setupDayActions();
        }
        
        this.updatePlayersGrid();
    }

    /**
     * Get night action text based on role
     */
    getNightActionText() {
        switch (this.myRole) {
            case 'werewolf':
                return 'Chọn người để giết';
            case 'seer':
                return 'Xem vai trò của một người';
            case 'witch':
                return 'Sử dụng thuốc (nếu có)';
            case 'guard':
                return 'Chọn người để bảo vệ';
            default:
                return 'Chờ đến lượt...';
        }
    }

    /**
     * Setup night action buttons
     */
    setupNightActions() {
        const actionButtons = document.getElementById('action-buttons');
        
        if (['werewolf', 'seer', 'witch', 'guard'].includes(this.myRole)) {
            actionButtons.innerHTML = `
                <button class="btn btn-primary" onclick="game.submitNightAction()">
                    ✅ Xác nhận hành động
                </button>
            `;
        } else {
            actionButtons.innerHTML = `
                <p style="color: #aaa;">🌙 Bạn là dân làng. Hãy chờ và quan sát...</p>
            `;
        }
    }

    /**
     * Setup day action buttons
     */
    setupDayActions() {
        const actionButtons = document.getElementById('action-buttons');
        actionButtons.innerHTML = `
            <button class="btn btn-primary" onclick="game.submitVote()">
                🗳️ Bỏ phiếu
            </button>
        `;
    }

    /**
     * Update players grid
     */
    updatePlayersGrid() {
        const grid = document.getElementById('players-grid');
        const players = this.multiplayer.players;
        
        grid.innerHTML = players.map((player, index) => {
            const isDead = player.alive === false;
            const isSelected = this.selectedPlayer === player.id;
            
            return `
                <div class="player-card ${isDead ? 'dead' : ''} ${isSelected ? 'selected' : ''}" 
                     onclick="game.selectPlayer(${player.id})">
                    <div class="status">${isDead ? '☠️' : '✅'}</div>
                    <div class="avatar">👤</div>
                    <div style="font-weight: bold;">${player.name}</div>
                    <div style="color: #aaa; font-size: 0.9em;">#${index + 1}</div>
                </div>
            `;
        }).join('');
    }

    /**
     * Select a player for action
     */
    selectPlayer(playerId) {
        if (this.gameState !== 'playing') return;
        
        const player = this.multiplayer.players.find(p => p.id === playerId);
        if (!player || !player.alive) return;
        
        this.selectedPlayer = playerId;
        this.updatePlayersGrid();
    }

    /**
     * Submit night action
     */
    submitNightAction() {
        if (!this.selectedPlayer) {
            this.showNotification('❌ Chọn một người trước!');
            return;
        }
        
        this.multiplayer.sendNightAction(this.myPlayerId, this.myRole, this.selectedPlayer);
        this.showNotification('✅ Đã gửi hành động!');
        this.selectedPlayer = null;
        this.updatePlayersGrid();
    }

    /**
     * Submit vote
     */
    submitVote() {
        if (!this.selectedPlayer) {
            this.showNotification('❌ Chọn một người để bỏ phiếu!');
            return;
        }
        
        this.multiplayer.sendVote(this.myPlayerId, this.selectedPlayer);
        this.showNotification('✅ Đã bỏ phiếu!');
        this.selectedPlayer = null;
        this.updatePlayersGrid();
    }

    /**
     * Handle night action (host)
     */
    handleNightAction(data) {
        if (!this.multiplayer.isHost) return;
        
        // Store action
        if (!this.actionsReceived[data.role]) {
            this.actionsReceived[data.role] = [];
        }
        this.actionsReceived[data.role].push(data);
        
        this.addGameLog(`${data.playerName} (${this.ROLES[data.role].name}) đã hành động`);
    }

    /**
     * Handle vote (host)
     */
    handleVote(data) {
        if (!this.multiplayer.isHost) return;
        
        this.addGameLog(`${data.voterId} bỏ phiếu cho ${data.targetId}`);
    }

    /**
     * Send chat message
     */
    sendChat() {
        const input = document.getElementById('chat-input');
        const message = input.value.trim();
        
        if (!message) return;
        
        const player = this.multiplayer.players.find(p => p.id === this.myPlayerId);
        const playerName = player ? player.name : 'Anonymous';
        
        this.multiplayer.sendChatMessage(playerName, message);
        input.value = '';
    }

    /**
     * Handle chat input keypress
     */
    handleChatKey(event) {
        if (event.key === 'Enter') {
            this.sendChat();
        }
    }

    /**
     * Add chat message
     */
    addChatMessage(sender, message, timestamp) {
        const messagesDiv = document.getElementById('chat-messages');
        const time = new Date(timestamp).toLocaleTimeString('vi-VN', { 
            hour: '2-digit', 
            minute: '2-digit' 
        });
        
        messagesDiv.innerHTML += `
            <div class="chat-message">
                <div class="sender">${sender}</div>
                <div>${message}</div>
                <div class="time">${time}</div>
            </div>
        `;
        
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }

    /**
     * Add game log entry
     */
    addGameLog(message) {
        const logDiv = document.getElementById('game-log');
        logDiv.innerHTML += `
            <div class="chat-message">
                <div>${message}</div>
            </div>
        `;
        logDiv.scrollTop = logDiv.scrollHeight;
    }

    /**
     * Show notification
     */
    showNotification(message) {
        const notification = document.createElement('div');
        notification.className = 'notification';
        notification.textContent = message;
        document.body.appendChild(notification);
        
        setTimeout(() => notification.remove(), 3000);
    }
}

// Initialize game
const game = new WerewolfGame();

// Expose functions to HTML
window.createRoom = () => game.createRoom();
window.joinRoom = () => game.joinRoom();
window.copyRoomCode = () => game.copyRoomCode();
window.startGame = () => game.startGame();
window.selectPlayer = (id) => game.selectPlayer(id);
window.submitNightAction = () => game.submitNightAction();
window.submitVote = () => game.submitVote();
window.sendChat = () => game.sendChat();
window.handleChatKey = (e) => game.handleChatKey(e);
