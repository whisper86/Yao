function refresh(){
    var num = Math.floor(Math.random() * 5 + 1);
    var img = document.getElementById("code")
    var location = "../static/Sign_Up/code"+num+".png"
    img.src = location
}

function Sign_up(){
    alert("Success")
}