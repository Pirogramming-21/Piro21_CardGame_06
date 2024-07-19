document.addEventListener('DOMContentLoaded', function() {
    generateCardOptions();
});
// 카드 선택 옵션 생성
function generateCardOptions() {
    const cardSelection = document.getElementById('yty_card-selection');
    if (cardSelection) {
        const cards = cardSelection.querySelectorAll('.card');
        cards.forEach(card => {
            card.addEventListener('click', () => selectCard(card.dataset.value));
        });
    }
}

function selectCard(num) {
    console.log('Card value in selectCard function:', num); // 디버깅용
    // 현재 선택된 카드가 있다면 선택 상태를 제거
    const currentSelected = document.querySelector('#yty_card-selection .card.selected');
    if (currentSelected) {
        currentSelected.classList.remove('selected');
    }

    // 클릭된 카드에 선택 상태를 추가
    const selectedCard = document.querySelector(`#yty_card-selection .card[data-value='${num}']`);
    if (selectedCard) {
        selectedCard.classList.add('selected');
    }

    // 선택된 카드 값을 숨겨진 input 필드에 설정
    const selectedCardInput = document.getElementById('selected_card');
    if (selectedCardInput) {
        selectedCardInput.value = num;
    }

    // 선택된 카드 값 출력 또는 추가 작업 수행
    console.log('Selected card:', num);
}