console.log('hello intro course')

const modalBtns = [...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementById("modal-body-confirm");
const startBtn = document.getElementById("start-button");
const csrf = document.getElementsByName("csrfmiddlewaretoken");

modalBtns.forEach(modalBtns=>modalBtns.addEventListener('click', function() {
    const pk = modalBtns.getAttribute('data-pk');
    const name = modalBtns.getAttribute("data-name");
    const description = modalBtns.getAttribute("data-description");
    const created = modalBtns.getAttribute("data-created");
    const studentName = modalBtns.getAttribute("data-student");

    modalBody.innerHTML = `
        <div class="h5 mb-3">Bạn có muốn học "<b>${name}</b>" không?</div>
        <div class="text-muted">
            <ul>
                <li>Ngày tạo: <b>${created}</b></li>
                <li>Nội dung: <b>${description}</b></li>             
            </ul>
        </div>
    `;

    const sendData = () => {
        $.ajax({
            type: "POST",
            url: `http://127.0.0.1:8000/student/course/${pk}/save`,
            data: {
                studentName: studentName,
                courseId: pk,
                csrfmiddlewaretoken: csrf[0].value,
            },
            success: function (response) {
                console.log(response);
            },
            error: function (response) {
                console.log(response);
            },
        });
    }

    startBtn.addEventListener("click", () => {
        sendData();
        window.location.assign(`http://127.0.0.1:8000/student/course/${pk}`);
    });
}))