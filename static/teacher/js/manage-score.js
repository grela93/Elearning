console.log('HELLO MANAGE SCORE');

const modalBtns = [...document.getElementsByClassName('modal-button')];
const title = document.getElementById('scoreTitle');
const modalBody = document.getElementById('modal-body-confirm');
const url = window.location.href;

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', function() {
    const pk = modalBtn.getAttribute('data-pk');
    const name = modalBtn.getAttribute('data-name');
    modalBody.innerHTML = '';
    title.innerHTML = `Xem điểm bài Quiz của môn <strong>${name}</strong>`;

    $.ajax({
        type: 'GET',
        url: `${url}${pk}/data`,
        success: function(response) {
            const data = response.data;
            data.forEach(el => {
                for(const [quiz, id] of Object.entries(el)) {
                    modalBody.innerHTML += `
                        <p><button 
                        class='btn btn-primary btn-lg quiz-button'
                        data-pk="${id}"
                        style='width: 350px;'>
                        ${quiz}
                        </button>
                        </p>
                    `;
                }
                const btns = [...document.getElementsByClassName("quiz-button")];
                btns.forEach((btn) =>
                    btn.addEventListener("click", () => {
                        // console.log(btn)
                        const pk = btn.getAttribute("data-pk");
                        window.location.assign(
                          `http://127.0.0.1:8000/teacher/view-score/${pk}`
                        );
                    })
                )
            })
            console.log(response);
        },
        error: function(response) {
            console.log(response);
        }
    })
}))