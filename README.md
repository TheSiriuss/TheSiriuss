<div align="center">

<img src="assets/banner.svg" alt="Nikita Miroshnichenko, TheSiriuss: Rust, Go, applied cryptography, AI red teaming" width="100%">

<br>

<a href="https://github.com/TheSiriuss?tab=repositories&language=rust"><img alt="Rust" src="https://img.shields.io/badge/Rust-2b3a4a?style=for-the-badge&logo=rust&logoColor=ffb454"></a>
<a href="https://github.com/TheSiriuss?tab=repositories&language=go"><img alt="Go" src="https://img.shields.io/badge/Go-2b3a4a?style=for-the-badge&logo=go&logoColor=ffb454"></a>
<a href="https://github.com/TheSiriuss?tab=repositories&language=python"><img alt="Python" src="https://img.shields.io/badge/Python-2b3a4a?style=for-the-badge&logo=python&logoColor=ffb454"></a>
<img alt="C++" src="https://img.shields.io/badge/C%2B%2B-2b3a4a?style=for-the-badge&logo=cplusplus&logoColor=ffb454">
<img alt="Void Linux" src="https://img.shields.io/badge/Void%20Linux-2b3a4a?style=for-the-badge&logo=voidlinux&logoColor=ffb454">
<a href="https://t.me/NikitaGodfrey"><img alt="Telegram" src="https://img.shields.io/badge/Telegram-b8802a?style=for-the-badge&logo=telegram&logoColor=white"></a>

<br><br>

<i>I write Rust and Go: encrypted messengers, small desktop tools, shaders for fun.<br>I also like finding the places where safety filters break.</i>

</div>

<br>

<br>

<img src="assets/head-featured.svg" alt="Featured" width="100%">

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/TheSiriuss/embertarn"><img src="assets/card-embertarn.png" alt="Embertarn login screen: a night meadow and a painted cat, drawn in a terminal" width="100%"></a>
      <h3><a href="https://github.com/TheSiriuss/embertarn">Embertarn</a></h3>
      <sub><b>Go · peer-to-peer messenger for the terminal</b></sub><br>
      Messages go straight from peer to peer, end-to-end encrypted. Double Ratchet, XChaCha20-Poly1305, Kademlia DHT, QUIC with hole punching, voice and colour video, all drawn in a terminal.
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/TheSiriuss/chess-rt"><img src="assets/card-chess.png" alt="Chess on a raft in a koi pond at night, lit by paper lanterns" width="100%"></a>
      <h3><a href="https://github.com/TheSiriuss/chess-rt">chess-rt</a></h3>
      <sub><b>Rust · Slint · GLSL · chess on a koi pond</b></sub><br>
      The whole scene is one ray-traced fragment shader: soft shadows, water caustics, koi, lanterns, rain and lightning. Plays against Stockfish and other UCI engines.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/TheSiriuss/refind-cat"><img src="assets/card-refind.png" alt="The rEFInd boot menu with a painted cat in a night meadow" width="100%"></a>
      <h3><a href="https://github.com/TheSiriuss/refind-cat">refind-cat</a></h3>
      <sub><b>freestanding C · UEFI · an animated boot menu</b></sub><br>
      A 12 KB driver adds animation to rEFInd: a blinking cat, fireflies and twinkling stars painted into the framebuffer. Tested in QEMU with OVMF.
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/TheSiriuss/keyos-passphrase"><img src="assets/card-passphrase.png" alt="Three screens of the passphrase generator: dice entry, eight words with an entropy gauge, a finished passphrase" width="100%"></a>
      <h3><a href="https://github.com/TheSiriuss/keyos-passphrase">Passphrase for Passport Prime</a></h3>
      <sub><b>Rust · Slint · diceware for a hardware wallet OS</b></sub><br>
      Words are drawn from the hardware RNG without bias and overwritten in memory afterwards. The screen covers them after 30 s and wipes after 120 s. The app works offline and keeps nothing on disk.
    </td>
  </tr>
</table>

<br>

<img src="assets/head-embertarn.svg" alt="How Embertarn finds your friend" width="100%">

<img src="assets/flow.svg" alt="Three steps: 1. look up the friend's PeerID in the Kademlia DHT, 2. connect directly over QUIC or TCP with hole punching, 3. talk with Double Ratchet, a fresh key for every message. Once, over a channel you trust, compare the fingerprint and the short code." width="100%">

<br>

<img src="assets/head-work.svg" alt="What I work on" width="100%">

<table>
  <tr>
    <td width="25%" align="center" valign="top">
      <br><img src="assets/icon-crypto.svg" alt="" width="84"><br><br>
      <b>Applied cryptography</b><br>
      <sub><a href="https://github.com/TheSiriuss/embertarn">Embertarn</a>: Double Ratchet, XChaCha20-Poly1305, Argon2id.<br><a href="https://github.com/TheSiriuss/keyos-passphrase">Passphrase</a>: hardware RNG, wiped memory.</sub>
    </td>
    <td width="25%" align="center" valign="top">
      <br><img src="assets/icon-reverse.svg" alt="" width="84"><br><br>
      <b>Reverse engineering</b><br>
      <sub><a href="https://github.com/TheSiriuss/seiren-control">Seiren Control</a> re-implements a USB lighting protocol.<br><a href="https://github.com/TheSiriuss/emberrit-patcher">emberrit-patcher</a> and <a href="https://github.com/TheSiriuss/telegram-no-ads">telegram-no-ads</a> patch apps you supply.</sub>
    </td>
    <td width="25%" align="center" valign="top">
      <br><img src="assets/icon-audio.svg" alt="" width="84"><br><br>
      <b>Audio DSP</b><br>
      <sub><a href="https://github.com/TheSiriuss/seiren-control">Seiren Control</a>: RNNoise, DeepFilterNet3, EQ, limiter, EBU R128 loudness, a virtual microphone.</sub>
    </td>
    <td width="25%" align="center" valign="top">
      <br><img src="assets/icon-graphics.svg" alt="" width="84"><br><br>
      <b>Graphics</b><br>
      <sub><a href="https://github.com/TheSiriuss/chess-rt">chess-rt</a>, a ray-traced shader.<br><a href="https://github.com/TheSiriuss/refind-cat">refind-cat</a>, animation painted into the UEFI framebuffer.</sub>
    </td>
  </tr>
</table>

<br>

<img src="assets/head-languages.svg" alt="Languages" width="100%">

<img src="assets/langs.svg" alt="Languages across my public repositories: Rust 4, Go 3, Python 3, Shell 2" width="100%">

<details>
<summary><b>More repositories</b></summary>

<br>

| Repository | Language | What it is |
|:--|:--|:--|
| [embertarn](https://github.com/TheSiriuss/embertarn) | Go | Decentralised peer-to-peer messenger for the terminal |
| [chess-rt](https://github.com/TheSiriuss/chess-rt) | Rust | Chess on a raft in a koi pond, one ray-traced fragment shader |
| [seiren-control](https://github.com/TheSiriuss/seiren-control) | Rust | Linux control panel for the Razer Seiren V3 Chroma: lighting, recording, noise suppression, virtual mic |
| [keyos-passphrase](https://github.com/TheSiriuss/keyos-passphrase) | Rust | Diceware passphrase generator for the Passport Prime |
| [AV33-client](https://github.com/TheSiriuss/AV33-client) | Rust | Portable VPN client for Windows and Linux |
| [refind-cat](https://github.com/TheSiriuss/refind-cat) | Python, C | Animated night-meadow theme for rEFInd |
| [emberrit-patcher](https://github.com/TheSiriuss/emberrit-patcher) | Python | Builds an ad-free Reddit client from the APK you supply |
| [telegram-no-ads](https://github.com/TheSiriuss/telegram-no-ads) | Shell | Patch for Telegram Desktop that removes sponsored messages |
| [term-reader](https://github.com/TheSiriuss/term-reader) | Go | Terminal reader |
| [ASCII-camera-python](https://github.com/TheSiriuss/ASCII-camera-python) | Python | Webcam picture as ASCII art |

</details>

<br>

<img src="assets/footer.svg" alt="still awake, still watching the moon" width="100%">
