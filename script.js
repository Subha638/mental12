$(document).ready(function() {
    function appendMessage(sender, message) {
        var cls = sender === "user" ? "userMsg" : "aiMsg";
        $("#chatBox").append("<div class='" + cls + "'><b>" + sender + ":</b> <span class='text'></span></div>");
        return $("#chatBox .text").last();
    }

    $("#sendBtn").click(function() {
        var user_msg = $("#userMessage").val();
        if (user_msg.trim() === "") return;

        // Append user message
        appendMessage("You", user_msg).text(user_msg);
        $("#userMessage").val("");

        // Append AI message placeholder
        var aiTextElem = appendMessage("AI", "");

        // Send AJAX request
        $.post("/get_response", { message: user_msg }, function(data) {
            var reply = data.reply;
            var i = 0;

            // Typing animation
            var typing = setInterval(function() {
                if (i < reply.length) {
                    aiTextElem.append(reply[i]);
                    i++;
                    $("#chatBox").scrollTop($("#chatBox")[0].scrollHeight);
                } else {
                    clearInterval(typing);
                }
            }, 30); // typing speed in ms
        });
    });
});
