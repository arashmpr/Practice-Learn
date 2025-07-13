function updateTimestamp() {
    const now = new Date();
    const timestamp = now.toISOString().replace('T', ' ').slice(0, 19);
    document.querySelector('.auth-timestamp').textContent = 'UTC: ' + timestamp;
}
setInterval(updateTimestamp, 1000);
updateTimestamp();