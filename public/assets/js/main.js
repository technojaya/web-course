let count = 0
function buttonClicked() {
    console.log("clicked! " + count)
    document.getElementById("demo").style.color = "red";
    count = count + 1
}