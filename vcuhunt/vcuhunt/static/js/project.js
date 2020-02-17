/* Project specific Javascript goes here. */


<script>
    function openForm() {
        document.getElementById("quiz").style.display = "block";
    }
    
    function closeForm() {
        document.getElementById("quiz").style.display = "none";
    }

    function submitAnswer() {
    var radios = document.getElementsByName("Quiz Question");
    var i = 0, len = radios.length;
    var checked = false;
    var userAnswer;
    
    for( ; i < len; i++ ) {
        if(radios[i].checked) {
        checked = true;
        userAnswer = radios[i].value;
        }
    } 
    // if user click submit button without selecting any option, alert box should be say "please select choice answer".
    if(!checked) {
        alert("Please select an answer");
        return;
    }
    // Correct answer
    if(userAnswer === "maison") {
        alert("Answer is correct!");
    }
    // incorrect answer
    else {
        alert("Answer is wrong!");
    }
    
    }

</script>
{% endblock quizScript %}
<script>
    function openForm() {
        document.getElementById("quiz").style.display = "block";
    }
    
    function closeForm() {
        document.getElementById("quiz").style.display = "none";
    }

    function submitAnswer() {
    var radios = document.getElementsByName("Quiz Question");
    var i = 0, len = radios.length;
    var checked = false;
    var userAnswer;
    
    for( ; i < len; i++ ) {
        if(radios[i].checked) {
        checked = true;
        userAnswer = radios[i].value;
        }
    } 
    // if user click submit button without selecting any option, alert box should be say "please select choice answer".
    if(!checked) {
        alert("Please select an answer");
        return;
    }
    // Correct answer
    if(userAnswer === "maison") {
        alert("Answer is correct!");
    }
    // incorrect answer
    else {
        alert("Answer is wrong!");
    }
    
    }

</script>