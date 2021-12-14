function logMessage(msg)
{
        const xhr = new XMLHttpRequest();
        xhr.open('GET', './log/' + encodeURIComponent(msg), true);
        xhr.onerror = function () {
                alert("Failed to log: message" + msg)
        }
        xhr.send();
}