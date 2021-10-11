console.log("CREATE QUESITON BY DOCX");

const questionForm = document.getElementById("add-bydocx-form");
const questionDetail = document.getElementById("question-detail");
const csrf = document.getElementsByName("csrfmiddlewaretoken");
const url = window.location.href;
let stt = 1;

$.ajax({
    type: 'GET',
    url: `${url}/data`,
    success: function(response) {
        const data = response.data;
        console.log(data);
        if (data == 'nothing') {
            questionDetail.innerHTML = '<h5>Mời thêm file .docx</h5>';
        } else {
            questionDetail.innerHTML = "";
            data.forEach(el => {
                for (const [question, ans] of Object.entries(el)) {
                    questionDetail.innerHTML += `
                        <h5><strong>${stt}. ${question}</strong></h5>
                        <div class="row">
                            <p class="col-6"><strong>A.&nbsp;</strong>${ans["ansA"]}</p>
                            <p class="col-6"><strong>B.&nbsp;</strong>${ans["ansB"]}</p>
                            <p class="col-6"><strong>C.&nbsp;</strong>${ans["ansC"]}</p>
                            <p class="col-6"><strong>D.&nbsp;</strong>${ans["ansD"]}</p>
                            <p><strong>Đáp án đúng:&nbsp;</strong>${ans["correctAns"]}</p>
                        </div>
                        <hr>
                    `;
                    stt = stt + 1;
                }
            })
        }
    },
    error: function(response) {
        console.log(response);
    }
})

// const sendQuestion = () => {
//     const file = document.getElementById('fileQuiz');
//     let data = {};
//     data["csrfmiddlewaretoken"] = csrf[0].value;
//     data['file'] = file.value;

//     $.ajax({
//         type: 'POST',
//         url: `${url}/save`,
//         data: data,
//         success: function(response) {
//             console.log(response);
//         },
//         error: function(response) {
//             console.log(response);
//         },
//     })
// }

// questionForm.addEventListener('submit', (e)=>{
//     e.preventDefault();

//     console.log('oke')
// })