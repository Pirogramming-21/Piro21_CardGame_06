// 전역 변수
let selectedCard = null;
let selectedOpponentId = null;

// 카드 선택 옵션 생성
function generateCardOptions() {
    const cardSelection = document.getElementById('yty_card-selection');
    if (cardSelection) {
        const cards = cardSelection.querySelectorAll('.yty_btn');
        cards.forEach(card => {
            card.addEventListener('click', () => {
                console.log('Card clicked:', card.dataset.card);
                selectCard(card.dataset.card);
            });
        });
    } else {
        console.error('Card selection element not found');
    }
}

// 카드 선택
function selectCard(num) {
    selectedCard = num;
    console.log('Selected card:', selectedCard); // 디버깅을 위한 로그 추가
    const buttons = document.querySelectorAll('#yty_card-selection .yty_btn');
    buttons.forEach(button => {
        button.classList.remove('selected');
        if (button.dataset.card === num) {
            button.classList.add('selected');
        }
    });
}

// 상대방 선택
function selectOpponent(opponentId) {
    selectedOpponentId = opponentId;
    const buttons = document.querySelectorAll('#yty_opponent-buttons .yty_opponent');
    buttons.forEach(button => {
        button.classList.remove('selected');
        if (button.dataset.opponentId === opponentId) {
            button.classList.add('selected');
        }
    });
}

// 공격
function attack() {
    console.log('Attack function called. Selected card:', selectedCard);
    if (!selectedCard) {
        alert('카드를 선택해주세요.');
        return;
    }
    if (!selectedOpponentId) {
        alert('상대방을 선택해주세요.');
        return;
    }

    // Ajax
    fetch(URLS.attack, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            card: selectedCard,
            opponent: selectedOpponentId
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = URLS.result;
        } else {
            alert('공격에 실패했습니다: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('오류가 발생했습니다.');
    });
}

// 반격 처리
function counterAttack() {
    console.log('Counter attack function called. Selected card:', selectedCard);
    if (!selectedCard) {
        alert('카드를 선택해주세요.');
        return;
    }

    // Ajax
    fetch(URLS.counterAttack, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({
            card: selectedCard
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = URLS.result;
        } else {
            alert('반격에 실패했습니다: ' + data.message);
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('오류가 발생했습니다.');
    });
}

// CSRF 토큰
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// 페이지 로드 시 실행
document.addEventListener('DOMContentLoaded', function() {
    generateCardOptions();

    // 공격하기 버튼 클릭 이벤트
    const attackBtn = document.getElementById('yty_attack-btn');
    if (attackBtn) {
        attackBtn.addEventListener('click', attack);
    }

    // 반격하기 버튼 클릭 이벤트
    const counterAttackBtn = document.getElementById('yty_counter-attack-btn');
    if (counterAttackBtn) {
        counterAttackBtn.addEventListener('click', counterAttack);
    }

    // 상대방 선택 버튼 클릭 이벤트
    document.querySelectorAll('#yty_opponent-buttons .yty_opponent').forEach(button => {
        button.addEventListener('click', function () {
            selectOpponent(this.dataset.opponentId);
        });
    });
});