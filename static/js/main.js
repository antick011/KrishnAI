document.getElementById('askForm').addEventListener('submit', async function (e) {
  e.preventDefault();

  const message = document.getElementById('message').value.trim();
  const language = document.getElementById('language').value;

  const responseBox = document.getElementById('responseBox');
  const omAudio = document.getElementById('omAudio');

  responseBox.classList.add('hidden');
  responseBox.innerHTML = "🙏 Krishna is thinking...";

  omAudio.pause();
  omAudio.currentTime = 0;

  try {
    const res = await fetch('/ask', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({ message, language })
    });

    const data = await res.json();

    if (data.error) {
      responseBox.innerHTML = `❌ ${data.error}`;
    } else {
      responseBox.innerHTML = `
        <h3>🕉️ Response from Krishna:</h3>
        <p><strong>Verse No.:</strong> ${data.verse_id}</p>
        <p><strong>Verse:</strong> ${data.sanskrit}</p>
        <p><strong>Translation:</strong> ${data.translation}</p>
        <p><strong>Divine Message:</strong> ${data.response}</p>
      `;

      // 🕉️ Play Om sound
      omAudio.play().catch(() => {
        console.warn("User interaction required to play audio on some devices.");
      });
    }
  } catch (err) {
    responseBox.innerHTML = "⚠️ Error communicating with KrishnaAI.";
  }

  responseBox.classList.remove('hidden');
});
document.getElementById('message').addEventListener('input', () => {
  const omAudio = document.getElementById('omAudio');
  omAudio.pause();
  omAudio.currentTime = 0;
});
