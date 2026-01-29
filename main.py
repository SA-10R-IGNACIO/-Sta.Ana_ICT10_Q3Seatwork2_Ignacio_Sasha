from js import document

def compute_average(event=None):
    filipino = float(document.getElementById("filipino").value)
    english = float(document.getElementById("english").value)
    science = float(document.getElementById("science").value)
    math = float(document.getElementById("math").value)
    ss = float(document.getElementById("ss").value)

    average = (filipino + english + science + math + ss) / 5

    if average >= 90:
        result = "Excellent"
    elif average >= 75:
        result = "Passed"
    else:
        result = "Failed"

    document.getElementById("average").innerText = str(round(average, 2))
    document.getElementById("result").innerText = result

# Attach button click properly (THIS IS THE FIX)
document.getElementById("computeBtn").onclick = compute_average
