console.log('hello form add quiz');

const addQuizForm = document.getElementById('add-quiz-form');
const createManualBtn = document.getElementById('create-manual-button');
const createByDocxBtn = document.getElementById('create-bydocx-button');
const csrf = document.getElementsByName("csrfmiddlewaretoken");
const url = window.location.href;
let quizID = '';

const saveQuiz = function() {
    const name = document.getElementById('quizName');
    const numberQuestion = document.getElementById("numberQuestion");
    const time = document.getElementById("time");
    const requiredScore = document.getElementById("requiredScore");
    const difficulity = document.getElementById("difficulity");
    const showResult = document.getElementById("showResult");

    data = {};
    data["csrfmiddlewaretoken"] = csrf[0].value;
    data["name"] = name.value;
    data["numberQuestion"] = numberQuestion.value;
    data["time"] = time.value;
    data["requiredScore"] = requiredScore.value;
    data["difficulity"] = difficulity.value;
    data["showResult"] = showResult.value;

    $.ajax({
        type: "POST",
        url: `${url}save`,
        data: data,
        success: function (response) {
            quizID = response.quiz_id
            console.log(quizID);
        },
        error: function (response) {
            console.log(response);
        },
    });
}

addQuizForm.addEventListener('submit', (e)=> {
    e.preventDefault();

    saveQuiz();
});

createManualBtn.addEventListener('click', function() {
    window.location.assign(`http://127.0.0.1:8000/teacher/add-question-form/${quizID}`);
});

createByDocxBtn.addEventListener('click', function() {
    window.location.assign(`http://127.0.0.1:8000/teacher/add-question-bydocx/${quizID}`);
});