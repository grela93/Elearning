var myState = {
    pdf: null,
    currentPage: 1,
    zoom: 1
};

pdfjsLib.getDocument("/home/grela/Documents/Elearn_demo/uploads/pdf/AD_videos_and_photos_uploading_instructions.pdf").then(pdf => {
    myState.pdf = pdf
    render()
});

function render() {
    myState.pdf.getPage(myState.currentPage).then(page => {
        var canvas = document.getElementById("#pdf-render");
        var ctx = canvas.getContext("2d");
        var viewport = page.getViewport(myState.zoom)

        canvas.width = viewport.width;
        canvas.height = viewport.height;

        //rendering the page
        page.render({
            canvasContext: ctx,
            viewport: viewport
        })
    })
}