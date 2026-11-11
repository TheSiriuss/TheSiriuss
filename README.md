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

<img src="assets/divider.svg" alt="" width="100%">

## Featured

<table>
  <tr>
    <td width="50%" valign="top">
      <p align="center"><a href="https://github.com/TheSiriuss/embertarn"><img src="https://raw.githubusercontent.com/TheSiriuss/embertarn/main/docs/screens/login-new.png" alt="Embertarn login screen: an animated night meadow with a painted cat, drawn in a terminal" height="250"></a></p>
      <h3><a href="https://github.com/TheSiriuss/embertarn">Embertarn</a></h3>
      <sub><b>Go</b> · peer-to-peer messenger for the terminal</sub><br>
      Messages go straight from peer to peer, end-to-end encrypted. Double Ratchet, XChaCha20-Poly1305, Kademlia DHT, QUIC with hole punching, voice and colour video, all drawn in a terminal.
    </td>
    <td width="50%" valign="top">
      <p align="center"><a href="https://github.com/TheSiriuss/chess-rt"><img src="https://raw.githubusercontent.com/TheSiriuss/chess-rt/main/docs/night.jpg" alt="Chess on a raft in a koi pond at night, lit by paper lanterns" height="250"></a></p>
      <h3><a href="https://github.com/TheSiriuss/chess-rt">chess-rt</a></h3>
      <sub><b>Rust</b> · Slint · GLSL · chess on a koi pond</sub><br>
      The whole scene is one ray-traced fragment shader: soft shadows, water caustics, koi, lanterns, rain and lightning. Plays against Stockfish and other UCI engines.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <p align="center"><a href="https://github.com/TheSiriuss/refind-cat"><img src="https://raw.githubusercontent.com/TheSiriuss/refind-cat/main/docs/hero.jpg" alt="The rEFInd boot menu with an animated painted cat in a night meadow" height="250"></a></p>
      <h3><a href="https://github.com/TheSiriuss/refind-cat">refind-cat</a></h3>
      <sub><b>freestanding C</b> · UEFI · an animated boot menu</sub><br>
      A 12 KB driver adds animation to rEFInd: a blinking cat, fireflies and twinkling stars painted into the framebuffer. Tested in QEMU with OVMF.
    </td>
    <td width="50%" valign="top">
      <p align="center"><a href="https://github.com/TheSiriuss/keyos-passphrase"><img src="https://raw.githubusercontent.com/TheSiriuss/keyos-passphrase/main/screenshots/device-rng.png" alt="Passphrase generator on the Passport Prime simulator showing eight diceware words and an entropy gauge" height="250"></a></p>
      <h3><a href="https://github.com/TheSiriuss/keyos-passphrase">Passphrase for Passport Prime</a></h3>
      <sub><b>Rust</b> · Slint · a diceware generator for a hardware wallet OS</sub><br>
      Words are drawn from the hardware RNG without bias and overwritten in memory afterwards. The screen covers them after 30 s and wipes after 120 s. The app works offline and keeps nothing on disk.
    </td>
  </tr>
</table>

<img src="assets/divider.svg" alt="" width="100%">

## How Embertarn finds your friend

<img src="assets/flow.svg" alt="Three steps: 1. look up the friend's PeerID in the Kademlia DHT, 2. connect directly over QUIC or TCP with hole punching, 3. talk with Double Ratchet, a fresh key for every message. Once, over a channel you trust, compare the fingerprint and the short code." width="100%">

<img src="assets/divider.svg" alt="" width="100%">

## What I work on

| Area | Where to look |
|:--|:--|
| **Applied cryptography** | [Embertarn](https://github.com/TheSiriuss/embertarn): Double Ratchet, XChaCha20-Poly1305, an Argon2id-protected profile. [Passphrase](https://github.com/TheSiriuss/keyos-passphrase): hardware RNG and wiped memory. |
| **Reverse engineering** | [Seiren Control](https://github.com/TheSiriuss/seiren-control) re-implements a USB lighting protocol. [emberrit-patcher](https://github.com/TheSiriuss/emberrit-patcher) and [telegram-no-ads](https://github.com/TheSiriuss/telegram-no-ads) patch apps you supply. |
| **Audio DSP** | [Seiren Control](https://github.com/TheSiriuss/seiren-control): RNNoise, DeepFilterNet3, EQ, limiter, EBU R128 loudness. |
| **Graphics** | [chess-rt](https://github.com/TheSiriuss/chess-rt), a ray-traced shader. [refind-cat](https://github.com/TheSiriuss/refind-cat), an animation painted into the UEFI framebuffer. |

<img src="assets/divider.svg" alt="" width="100%">

## Languages

```text
Rust    ████████░░░░░░░░░░░░░░░░  4
Go      ██████░░░░░░░░░░░░░░░░░░  3
Python  ██████░░░░░░░░░░░░░░░░░░  3
Shell   ████░░░░░░░░░░░░░░░░░░░░  2
```

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

<div align="center">

<sub><i>still awake, still watching the moon</i></sub>

</div>
