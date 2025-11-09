
# Create webrtc.js - the main WebRTC and translation file (same as before)
webrtc_js = '''// WebRTC and Translation JavaScript for Voice Bridge FREE

const socket = io();
let localStream = null;
let peerConnection = null;
let isMuted = false;
let isTranslationEnabled = true;

const configuration = {
    iceServers: [
        { urls: 'stun:stun.l.google.com:19302' },
        { urls: 'stun:stun1.l.google.com:19302' }
    ]
};

const connectionStatus = document.getElementById('connectionStatus');
const micBtn = document.getElementById('micBtn');
const endCallBtn = document.getElementById('endCallBtn');
const myLanguageSelect = document.getElementById('myLanguage');
const translateToSelect = document.getElementById('translateTo');
const translationStatus = document.getElementById('translationStatus');
const participantList = document.getElementById('participantList');

async function initializeCall() {
    try {
        localStream = await navigator.mediaDevices.getUserMedia({
            audio: {
                echoCancellation: true,
                noiseSuppression: true,
                autoGainControl: true
            },
            video: false
        });
        
        connectionStatus.textContent = 'Connected to room';
        connectionStatus.classList.add('text-success');
        
        socket.emit('join', {
            room: roomCode,
            username: username
        });
        
        setupPeerConnection();
        
    } catch (error) {
        console.error('Error accessing media devices:', error);
        connectionStatus.textContent = 'Failed to access microphone';
        connectionStatus.classList.add('text-danger');
    }
}

function setupPeerConnection() {
    peerConnection = new RTCPeerConnection(configuration);
    
    localStream.getTracks().forEach(track => {
        peerConnection.addTrack(track, localStream);
    });
    
    peerConnection.ontrack = (event) => {
        const remoteAudio = document.getElementById('remoteAudio');
        const audioElement = document.createElement('audio');
        audioElement.srcObject = event.streams[0];
        audioElement.autoplay = true;
        audioElement.controls = false;
        remoteAudio.innerHTML = '';
        remoteAudio.appendChild(audioElement);
        
        connectionStatus.textContent = 'Call Active';
        
        if (isTranslationEnabled) {
            processAudioForTranslation(event.streams[0]);
        }
    };
    
    peerConnection.onicecandidate = (event) => {
        if (event.candidate) {
            socket.emit('ice-candidate', {
                room: roomCode,
                candidate: event.candidate
            });
        }
    };
    
    peerConnection.onconnectionstatechange = () => {
        console.log('Connection state:', peerConnection.connectionState);
        if (peerConnection.connectionState === 'disconnected') {
            connectionStatus.textContent = 'Disconnected';
            connectionStatus.classList.remove('text-success');
            connectionStatus.classList.add('text-warning');
        }
    };
}

function processAudioForTranslation(stream) {
    const mediaRecorder = new MediaRecorder(stream);
    const audioChunks = [];
    
    mediaRecorder.ondataavailable = (event) => {
        audioChunks.push(event.data);
    };
    
    mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
        
        const formData = new FormData();
        formData.append('audio', audioBlob);
        formData.append('source_lang', myLanguageSelect.value);
        formData.append('target_lang', translateToSelect.value);
        
        try {
            translationStatus.textContent = '🔄 Translating (FREE APIs)...';
            translationStatus.classList.remove('alert-info');
            translationStatus.classList.add('alert-warning');
            
            const response = await fetch('/translate-audio', {
                method: 'POST',
                body: formData
            });
            
            if (response.ok) {
                const data = await response.json();
                translationStatus.textContent = `✅ Translated: ${data.translation}`;
                translationStatus.classList.remove('alert-warning');
                translationStatus.classList.add('alert-success');
                
                // Play translated audio
                if (data.audio) {
                    const audioData = atob(data.audio);
                    const arrayBuffer = new ArrayBuffer(audioData.length);
                    const view = new Uint8Array(arrayBuffer);
                    for (let i = 0; i < audioData.length; i++) {
                        view[i] = audioData.charCodeAt(i);
                    }
                    const blob = new Blob([arrayBuffer], { type: 'audio/mp3' });
                    const audioUrl = URL.createObjectURL(blob);
                    const audio = new Audio(audioUrl);
                    audio.play();
                }
            }
        } catch (error) {
            console.error('Translation error:', error);
            translationStatus.textContent = '❌ Translation error';
            translationStatus.classList.add('alert-danger');
        }
        
        audioChunks.length = 0;
    };
    
    setInterval(() => {
        if (mediaRecorder.state === 'recording') {
            mediaRecorder.stop();
        }
        mediaRecorder.start();
        setTimeout(() => mediaRecorder.stop(), 3000);
    }, 3500);
}

socket.on('user-connected', async (data) => {
    console.log('User connected:', data.username);
    
    const li = document.createElement('li');
    li.className = 'list-group-item';
    li.textContent = data.username;
    participantList.appendChild(li);
    
    const offer = await peerConnection.createOffer();
    await peerConnection.setLocalDescription(offer);
    
    socket.emit('offer', {
        room: roomCode,
        offer: offer
    });
});

socket.on('offer', async (data) => {
    await peerConnection.setRemoteDescription(new RTCSessionDescription(data.offer));
    
    const answer = await peerConnection.createAnswer();
    await peerConnection.setLocalDescription(answer);
    
    socket.emit('answer', {
        room: roomCode,
        answer: answer
    });
});

socket.on('answer', async (data) => {
    await peerConnection.setRemoteDescription(new RTCSessionDescription(data.answer));
});

socket.on('ice-candidate', async (data) => {
    try {
        await peerConnection.addIceCandidate(new RTCIceCandidate(data.candidate));
    } catch (error) {
        console.error('Error adding ICE candidate:', error);
    }
});

socket.on('user-disconnected', (data) => {
    console.log('User disconnected:', data.username);
    connectionStatus.textContent = 'User disconnected';
});

socket.on('language-updated', (data) => {
    console.log(`${data.username} changed language to ${data.language}`);
});

micBtn.addEventListener('click', () => {
    isMuted = !isMuted;
    localStream.getAudioTracks().forEach(track => {
        track.enabled = !isMuted;
    });
    
    micBtn.textContent = isMuted ? '🎤 Unmute' : '🎤 Mute';
    micBtn.classList.toggle('btn-warning');
});

endCallBtn.addEventListener('click', () => {
    if (confirm('End call?')) {
        socket.emit('leave', {
            room: roomCode,
            username: username
        });
        
        if (localStream) {
            localStream.getTracks().forEach(track => track.stop());
        }
        
        if (peerConnection) {
            peerConnection.close();
        }
        
        window.location.href = '/dashboard';
    }
});

myLanguageSelect.addEventListener('change', () => {
    socket.emit('language-change', {
        room: roomCode,
        username: username,
        language: myLanguageSelect.value
    });
});

translateToSelect.addEventListener('change', () => {
    console.log('Translation target changed to:', translateToSelect.value);
});

window.addEventListener('beforeunload', () => {
    socket.emit('leave', {
        room: roomCode,
        username: username
    });
});

initializeCall();'''

with open(f"{base_dir}/static/js/webrtc.js", 'w') as f:
    f.write(webrtc_js)

print("✅ Created webrtc.js with FREE translation integration!")
