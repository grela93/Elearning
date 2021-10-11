console.log("hello intro quiz");

const modalQuizBtns = [...document.getElementsByClassName('modal-quiz-button')];
const modalBodyQuiz = document.getElementById('modal-body-quiz');
const startQuizBtn = document.getElementById('start-button');
const hostname = window.location.hostname

modalQuizBtns.forEach(modalQuizBtns=> modalQuizBtns.addEventListener('click', ()=>{
    // console.log(modalBtns)
    const pk = modalQuizBtns.getAttribute('data-pk');
    const name = modalQuizBtns.getAttribute('data-name');
    const numQuestions = modalQuizBtns.getAttribute('data-questions');
    const difficulity = modalQuizBtns.getAttribute('data-difficulity');
    const scoreToPass = modalQuizBtns.getAttribute('data-pass');
    const time = modalQuizBtns.getAttribute('data-time');
    const result = modalQuizBtns.getAttribute('data-result');
    
    modalBodyQuiz.innerHTML = `
        <div class="h5 mb-3">Bạn có chắc chắn làm "<b>${name}</b>" không?</div>
        <div class="text-muted">
            <ul>
                <li>Số câu: <b>${numQuestions}</b></li>
                <li>Độ khó: <b>${difficulity}</b></li>
                <li>Điểm cần đạt: <b>${scoreToPass}</b></li>
                <li>Thời gian: <b>${time} phút</b></li>  
                <li>Hiển thị kết quả: <b>${result}</b></li>              
            </ul>
        </div>
    `;

    startQuizBtn.addEventListener('click', ()=>{
        window.location.assign(`http://127.0.0.1:8000/student/quiz/${pk}`);
    });
}))