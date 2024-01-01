alert("此为Mr Xu 的作品，请尊重他人的知识产权")

function Img_Operation() {
    // 设置随机出现的文字数组
    var arr = ["啊，许垚真帅", "这世界欠了你太多的温柔",
        "少言自寡，胜过千言万语", "人间忽晚，山河已秋",
        "除了你自己，没人会时刻在意你", "温柔也是好多委屈换来的",
        "山茶花的红终究抵不过大海深处的群青",
        "崩溃都是悄无声息", "过树穿花踏遍山河，终要与你相逢"]
    document.onclick = function (x) {
        // 创建元素节点对象
        var span = document.createElement("span")
        // 获取当前鼠标的坐标
        span.style.left = x.clientX + "px"
        span.style.top = x.clientY + "px"
        // 让span的值为arr数组内随机的一个值
        span.innerHTML = arr[Math.floor(Math.random() * arr.length)]
        // span.innerHTML = arr[0]
        // 设置span的动画效果
        setTimeout(function () {
            span.style.opacity = "1"
            span.style.transform = "translateY(-100px)"
        }, 100)
        setTimeout(function () {
            span.style.opacity = "0"
            span.style.transform = "translate(-100px,-100px)"
        }, 2000)
        // 清掉opacort为0的span
        var chi = document.getElementsByClassName("span")
        for (var i = 0; i < chi.length; i++) {
            if (chi[i].style.opacity === "0") {
                document.body.removeChild(chi[i])
            }
        }
        // 将span添加到body里
        document.body.appendChild(span)
    }
}
function PullImg() {
    document.getElementById('dropdown-content-connect').innerHTML ="<img id='QR_Code' src='../static/images/QR_code.jpg' alt='二维码' style='width: 250px; height: 250px;'>"
    var chi = document.getElementById('QR_Code')
    console.log(chi)
    alert("你只有10s时间获得联系方式")
    setTimeout(function (){
        chi.remove()
    }, 10000)

}
