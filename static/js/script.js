function a(){
    console.log("test");
}

function redirect() {
    let url="/capture";
    console.log("Redirecting to: " + url);
    window.location.href = url;
}

function send(x) {
    redirect();
    $.ajax({
        url: '/data',
        method: "POST",
        data: {
            interval: x
        },
        success: function(result) {
            console.log("Transmission successful!");
        },
        error: function(error) {
            console.log("Error: " + error);
        }
    })
}

function send2(x) {
    redirect();
    $.post("/data", {"interval": x});
}
