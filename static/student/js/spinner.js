console.log("hello spinner");

const courseDetail = document.getElementById("course-detail");
const spinnerBody = document.getElementById('spinner-box-body')
const spinnerBox = document.getElementById('spinner-box');
const cmtBox = document.getElementsByClassName('cmt-box');
const cmtForm = document.getElementById('post-cmt');
const csrf = document.getElementsByName('csrfmiddlewaretoken');
const urlPage = window.location.href;

courseDetail.classList.add('not-visible');
setTimeout(() => {
    spinnerBody.classList.add('not-visible');
    courseDetail.classList.remove("not-visible");
}, 500);


$.ajax({
    type: "GET",
    url: urlPage + "/cmt",
    success: function(response) {
        setTimeout(() => {
            spinnerBox.classList.add("not-visible");
            console.log(response)
            for (const item of response) {
                if (item.student_name) {
                    cmtBox[0].innerHTML += `
                        <div class="cmt-heading">
                            <a class="cmt-author" href="#">${item.student_name}</a>&nbsp;&nbsp;<strong>${item.created_at}</strong>
                        </div>
                        <div class="cmt-body">${item.body}</div>
                        <hr>
                    `;
                } else {
                    cmtBox[0].innerHTML += `
                        <div class="cmt-heading">
                            <a class="cmt-author" href="#">${item.teacher_name}</a>&nbsp;&nbsp;<strong>${item.created_at}</strong>
                        </div>
                        <div class="cmt-body">${item.body}</div>
                        <hr>
                    `;
                }
                
            }
        }, 500);
    },
    error: function(response) {
        console.log(response)
    }
});

const sendData = () => {
    const bodyCmt = document.getElementById('body')
    const data = {};
    data['csrfmiddlewaretoken'] = csrf[0].value;
    data['body'] = bodyCmt.value;

    $.ajax({
        type: 'POST',
        url: urlPage + "/save-cmt",
        data: data,
        success: function(response) {
            if (response.body != '') {
                const studentName = response.studentName;
                const body = response.body;
                const created = response.time;

                cmtBox[0].innerHTML += `
                        <div class="cmt-heading">
                            <a class="cmt-author" href="#">${studentName}</a>&nbsp;&nbsp;<strong>${created}</strong>
                        </div>
                        <div class="cmt-body">${body}</div>
                        <hr>
                    `;
            }
            console.log(response);
        },
        error: function(response) {
            console.log(response);
        }
    })
}

cmtForm.addEventListener('submit', function(e) {
    e.preventDefault();
    spinnerBox.classList.remove("not-visible")
    setTimeout(() => {
        spinnerBox.classList.add("not-visible");
    }, 500);
    sendData();
})