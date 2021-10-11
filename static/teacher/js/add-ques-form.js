console.log('CREATE QUESTION MANUALLY!');

const questionForm = document.getElementById('add-manual-form');
const questionDetail = document.getElementById('question-detail');
const csrf = document.getElementsByName('csrfmiddlewaretoken');
const url = window.location.href;
let stt = 1;


const sendQuestion = () => {
    const question = document.getElementById('question');
    const ansA = document.getElementById('answerA');
    const ansB = document.getElementById('answerB');
    const ansC = document.getElementById("answerC");
    const ansD = document.getElementById("answerD");
    const correctAns = document.getElementById("correctAns")
    let data = {};

    data['csrfmiddlewaretoken'] = csrf[0].value;
    data['question'] = question.value;
    data['ansA'] = ansA.value;
    data["ansB"] = ansB.value;
    data["ansC"] = ansC.value;
    data["ansD"] = ansD.value;
    data["correctAns"] = correctAns.value;

    $.ajax({
        type: 'POST',
        url: `${url}/save`,
        data: data,
        success: function(response) {
            const data = response.data;
            questionDetail.innerHTML += `
                <h5><strong>${stt}. ${data['question'][0]}</strong></h5>
                <div class="row">
                    <p class="col-6"><strong>A.&nbsp;</strong>${data['ansA'][0]}</p>
                    <p class="col-6"><strong>B.&nbsp;</strong>${data['ansB'][0]}</p>
                    <p class="col-6"><strong>C.&nbsp;</strong>${data['ansC'][0]}</p>
                    <p class="col-6"><strong>D.&nbsp;</strong>${data['ansD'][0]}</p>
                    <p><strong>Đáp án đúng:&nbsp;</strong>${data['correctAns'][0]}</p>
                </div>
                <hr>
            `;
            stt = stt + 1;
        },
        error: function(response) {
            console.log(response);
        }
    })
}

questionForm.addEventListener('submit', (e) => {
    e.preventDefault();

    sendQuestion();
})
