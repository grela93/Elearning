console.log('list quiz');
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
            const cookies = document.cookie.split(";");
            for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const showBtn = [...document.getElementsByClassName('show-quiz-button')];
const quizList = document.getElementById('quiz-list');
const addQuiz = document.getElementById('add-quiz-btn');
const arrows = [...document.getElementsByClassName("arrow-icon")];
const url = window.location.href;
const csrf = document.getElementsByName('csrfmiddlewaretoken');

showBtn.forEach(showBtn=> showBtn.addEventListener('click', function() {
    const pk = showBtn.getAttribute("data-pk");
    const quiz = showBtn.getAttribute("data-quiz");
    const arrowId = document.getElementById(`${pk}`);

    arrows.forEach(e => {
        e.classList.remove("bx-fade-right", "arrow-active");
    })
    arrowId.classList.add("bx-fade-right", "arrow-active");

    $.ajax({
        type: 'GET',
        url: `${url}${pk}/data`,
        success: function(response) {
            const quizzes = response.quizzes;
            quizList.innerHTML = '';
            addQuiz.innerHTML = `<a href="http://127.0.0.1:8000/teacher/add-quiz/${pk}" class='btn btn-primary my-2'><i class='bx bx-plus-circle'></i>&nbsp;&nbsp;Thêm bài quiz</a>`;
            if (quizzes != '') {
                quizzes.forEach(el => {
                    for(const [quiz, quiz_id] of Object.entries(el)) {
                        quizList.innerHTML += `
                            <div id='quiz-detail' class='row my-2'>
                                <div class='col-8'><h5 class='mt-2'>${quiz}</h5></div>
                                
                                <span class='col-4 d-flex justify-content-center'>
                                <button 
                                    class='btn btn-outline-danger modal-button'
                                    data-pk="${quiz_id}"
                                    data-name="${quiz}"
                                    data-bs-toggle="modal"
                                    data-bs-target="#delQuizModal"
                                >
                                    Xóa
                                </button></span>
                            </div>
                            
                        `;
                    }
                    const modalBtns = [...document.getElementsByClassName("modal-button")];
                    const modalBody = document.getElementById("modal-quiz-confirm");
                    const delBtn = document.getElementById("del-button");

                    modalBtns.forEach((modalBtns) =>
                        modalBtns.addEventListener("click", () => {
                            // console.log(modalBtns)
                            const pk = modalBtns.getAttribute("data-pk");
                            const name = modalBtns.getAttribute("data-name");

                            modalBody.innerHTML = `
                                <div class="h5 mb-3 mx-3">Bạn có muốn xóa "<b>${name}</b>" không?</div>
                            `;
                            delBtn.addEventListener("click", () => {
                                $.ajax({
                                    url: `http://127.0.0.1:8000/teacher/delete-quiz/${pk}`,
                                    type: "DELETE",
                                    dataType: "json",
                                    headers: {
                                        "X-Requested-With": "XMLHttpRequest",
                                        "X-CSRFToken": getCookie("csrftoken"),
                                    },
                                    success: (data) => {
                                        console.log(data);
                                    },
                                    error: (error) => {
                                        console.log(error);
                                    },
                                });
                            });
                        })
                    );
                })
            }
        },
        error: function(response) {
            console.log(response);
        },
    })
}));

