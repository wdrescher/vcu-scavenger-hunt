/* Project specific Javascript goes here. */

function initMap() {
    // Your Location
    const loc = { lat: 42.361145, lng: -71.057083 };
    // Centered map on location
    const map = new google.maps.Map(document.querySelector('.map')
    , {
        zoom: 14,
        center: loc
    });
    // The marker, positioned at location
    const marker = new google.maps.Marker({ position: loc, map: map});
}

<script>
    function openform() {
        document.getelementbyid("quiz").style.display = "block";
    }
    
    function closeform() {
        document.getelementbyid("quiz").style.display = "none";
    }

    function submitanswer() {
    var radios = document.getelementsbyname("quiz question");
    var i = 0, len = radios.length;
    var checked = false;
    var useranswer;
    
    for( ; i < len; i++ ) {
        if(radios[i].checked) {
        checked = true;
        useranswer = radios[i].value;
        }
    } 
    // if user click submit button without selecting any option, alert box should be say "please select choice answer".
    if(!checked) {
        alert("please select an answer");
        return;
    }
    // correct answer
    if(useranswer === "maison") {
        alert("answer is correct!");
    }
    // incorrect answer
    else {
        alert("answer is wrong!");
    }
    
    }

</script>
{% endblock quizscript %}
<script>
    function openform() {
        document.getelementbyid("quiz").style.display = "block";
    }
    
    function closeform() {
        document.getelementbyid("quiz").style.display = "none";
    }

    function submitanswer() {
    var radios = document.getelementsbyname("quiz question");
    var i = 0, len = radios.length;
    var checked = false;
    var useranswer;
    
    for( ; i < len; i++ ) {
        if(radios[i].checked) {
        checked = true;
        useranswer = radios[i].value;
        }
    } 
    // if user click submit button without selecting any option, alert box should be say "please select choice answer".
    if(!checked) {
        alert("please select an answer");
        return;
    }
    // correct answer
    if(useranswer === "maison") {
        alert("answer is correct!");
    }
    // incorrect answer
    else {
        alert("answer is wrong!");
    }
    
    }

</script>