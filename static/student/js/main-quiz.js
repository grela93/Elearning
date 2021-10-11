console.log('hello quiz detail');
const url = window.location.href;

const quizBox = document.getElementById('quiz-box');
const scoreBox = document.getElementById('score-box');
const resultBox = document.getElementById('result-box');
const timerBox = document.getElementById('timer-box');
const spinnerBox = document.getElementById("spinner-box");
let stt = 1;

spinnerBox.classList.add('not-visible');
scoreBox.classList.add('not-visible');

// let timeDone;

const activateTimer = (time) => {
    if (time.toString().length < 2) {
        timerBox.innerHTML = `<b>0${time}:00</b>`;
    } else {
        timerBox.innerHTML = `<b>${time}:00</b>`;
    }
    let minutes = time - 1;
    let seconds = 60;
    let displaySeconds;
    let displayMinutes;
    let minutesDone;
    let secondDone;

    const timer = setInterval(() => {
        seconds --;
        if(seconds < 0) {
            seconds = 59;
            minutes --;            
        }

        if (minutes.toString().length < 2) {
            displayMinutes = '0' + minutes;
        } else {
            displayMinutes = minutes;
        }

        if (seconds.toString().length < 2) {
            displaySeconds = '0' + seconds;
        } else {
            displaySeconds = seconds;
        }

        if (minutes === 0 && seconds === 0) {
            timerBox.innerHTML = "<b>00:00</b>";
            setTimeout(() => {
                clearInterval(timer);
                alert('Hết thời gian làm bài');
                sendData();
            }, 500);            
        }

        timerBox.innerHTML = `<b>${displayMinutes}:${displaySeconds}</b>`
    }, 1000);

    // minutesDone = minutes - displayMinutes;
    // secondDone = 60 - displaySeconds;
    // timeDone = `${minutesDone}:${secondDone}`;

}

$.ajax({
    type: 'GET',
    url: `${url}/data`,
    success: function(response) {
        // console.log(response);
        const data = response.data;
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)) {
                quizBox.innerHTML += `
                <div class="border-top border-primary my-3 w-100"></div>        
                <div class="ml-4 mb-2">
                    <b>${stt}. ${question}</b>
                </div>
                `;
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                        <div>
                            <input type="radio" class="ans ml-2 mr-1" id="${question}-${answer}" name="${question}" value="${answer}">
                            <label for="${question}-${answer}">${answer}</label>
                        </div>
                    `;
                });
                stt = stt + 1;
            }
        });
        activateTimer(response.time);
    },
    error: function(error) {
        console.log(error)
    }
});

const quizForm = document.getElementById('quiz-form');
const csrf = document.getElementsByName('csrfmiddlewaretoken');

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')];
    const data = {};
    data['csrfmiddlewaretoken'] = csrf[0].value;
    elements.forEach(el => {
        if (el.checked) {
            data[el.name] = el.value;
        } else {
            if (!data[el.name]) {
                data[el.name] = null;
            }
        }
    });

    $.ajax({
        type: 'POST',
        url: `${url}/save`,
        data: data,
        success: function (response) {
            // console.log(response);
            const results = response.results;
            console.log(results);
            quizForm.classList.add('not-visible');
            scoreBox.classList.remove("not-visible");

            scoreBox.innerHTML = `
                <p>Điểm: ${response.score.toFixed(2)}</p>
                <p>${
                response.passed
                    ? "Chúc mừng bạn đã đủ điểm qua bài kiểm tra!"
                    : "Thiếu điểm mất rồi, cố gắng vào lần sau nhé!"
                }</p>         
            `;

            results.forEach(res => {
                const resDiv = document.createElement("div");
                for (const [question, resp] of Object.entries(res)){                    
                    resDiv.innerHTML += question;
                    const cls = ['container', 'p-3', 'text-light', 'h6', 'my-3'];
                    resDiv.classList.add(...cls);

                    if (resp == 'not answered') {
                        resDiv.classList.add('bg-danger');
                        resDiv.innerHTML += ' ----- Không chọn đáp án';
                    } else {
                        const answer = resp['answered'];
                        const correct = resp['correct_answer'];
                        
                        if (answer == correct) {
                            resDiv.classList.add('bg-success');
                            resDiv.innerHTML += ` ----- Đáp án đúng: ${answer}`;
                        } else {
                            resDiv.classList.add('bg-danger');
                            resDiv.innerHTML += ` ----- Đáp án đúng: ${correct}`;
                            resDiv.innerHTML += ` | Bạn chọn: ${answer}`;
                        }
                    }
                }
                // const body_content = document.getElementById('body-content');
                resultBox.append(resDiv);
                timerBox.innerHTML = "<b>00:00</b>";
            })
        },
        error: function (error) {
            console.log(error);
        }
    })
};

quizForm.addEventListener('submit', e => {
    e.preventDefault();
    spinnerBox.classList.remove("not-visible");
    setTimeout(() => {
        spinnerBox.classList.add("not-visible");
        sendData();               
    }, 500);
})