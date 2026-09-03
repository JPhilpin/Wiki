---
title: 3D Thinking is just the start
slug: the-tesseract
summary: ""
tags:
- solid-thinking
- the-tesseract
aliases: []
pstatus: unknown
---


See Also: [The Full Picture](https://wiki.philpin.com/tesseract.html)

	
<div class="complex">
 <!-- LEFT COLUMN: canvas -->
 <div class="complex-left ">
 <canvas id="c"></canvas>
 </div>

 <!-- RIGHT COLUMN: text -->
 <div class="complex-right">
 <h2>Dynamics of Complexity</h2>
 <p>The rotation you see here is a <strong>4D projection</strong> being simplified into <strong>2D space</strong>. This dynamic visualization serves as a metaphor for the way complex systems interact within the Tesseract framework.</p>

 <p>A <strong>Tesseract</strong>, or hypercube, is the four-dimensional equivalent of a standard three-dimensional cube. To understand it, think of how a 3D cube relates to a 2D square: a square is made of four lines, and a cube is made of six squares; similarly, a Tesseract is constructed from eight full cubes. Since we cannot perceive the fourth dimension directly, we can only visualize a Tesseract through its three-dimensional projection, which often appears as two nesting or overlapping cubes. When mathematicians “rotate” a Tesseract, the resulting projection appears to twist, overlap, and change shape in ways that seem impossible, but this paradoxical movement is simply our way of processing its complex four-dimensional geometry.</p>

 <h2>Tesseract Thinking</h2>
 <p>The Tesseract represents the conceptual framework for understanding the relationships and interactions that exist beyond simple linear cause-and-effect (the 3D world). It is the space where our Structured Thinking model accounts for complexity and emergent behavior.</p>

 <h2>Summary:</h2>
 <ul>
 <li><strong>Emergent Behaviors:</strong> Results greater than the sum of the system's parts.</li>
 <li><strong>Non-Linear Forces:</strong> Where small inputs lead to disproportionately large, unpredictable outputs.</li>
 </ul>
 <p>Its constantly changing geometry represents the market and organizational complexity that the Structured Thinking model must address.</p>
 </div>
</div>

<script>
 const canvas = document.getElementById("c");
 const ctx = canvas.getContext("2d");

 function resizeCanvas() {
 const aspect = 16 / 9;
 let w = canvas.parentElement.clientWidth;
 let h = w / aspect;
 if (h > window.innerHeight * 0.85) {
 h = window.innerHeight * 0.85;
 w = h * aspect;
 }
 canvas.width = w;
 canvas.height = h;
 }
 resizeCanvas();
 window.addEventListener("resize", resizeCanvas);

 const palette = ["#252941","#FFBF00","#DC1143","#125993","#7A8F99","#E5E5E7"];
 const lineColors = palette.slice(1);

 function hexToRGB(hex) {
 const h = hex.replace("#", "");
 return {
 r: parseInt(h.slice(0, 2), 16),
 g: parseInt(h.slice(2, 4), 16),
 b: parseInt(h.slice(4, 6), 16),
 };
 }

 function lighten(hex, amt = 0.35) {
 const { r, g, b } = hexToRGB(hex);
 const nr = Math.min(255, Math.floor(r + (255 - r) * amt));
 const ng = Math.min(255, Math.floor(g + (255 - g) * amt));
 const nb = Math.min(255, Math.floor(b + (255 - b) * amt));
 return (
 "#" +
 nr.toString(16).padStart(2, "0") +
 ng.toString(16).padStart(2, "0") +
 nb.toString(16).padStart(2, "0")
 );
 }

 const base = [];
 const vals = [-1, 1];
 for (let x of vals) {
 for (let y of vals) {
 for (let z of vals) {
 for (let w of vals) {
 base.push([x, y, z, w]);
 }
 }
 }
 }

 const edges = [];
 for (let i = 0; i < base.length; i++) {
 for (let j = i + 1; j < base.length; j++) {
 const a = base[i], b = base[j];
 let diff = 0;
 if (a[0] !== b[0]) diff++;
 if (a[1] !== b[1]) diff++;
 if (a[2] !== b[2]) diff++;
 if (a[3] !== b[3]) diff++;
 if (diff === 1) edges.push([i, j]);
 }
 }

 const faces = [
 [0, 1, 3, 2],
 [4, 5, 7, 6],
 [8, 9, 11, 10],
 [12, 13, 15, 14]
 ];

 let angXW = 0, angYW = 0, angZW = 0, angXY = 0, tick = 0;

 function rot4(p, i, j, a) {
 const s = Math.sin(a);
 const c = Math.cos(a);
 const pi = p[i];
 const pj = p[j];
 p[i] = pi * c - pj * s;
 p[j] = pi * s + pj * c;
 }

 function draw() {
 tick++;

 const W = canvas.width;
 const H = canvas.height;
 const CX = W / 2;
 const CY = H / 2;
 const SCALE = Math.min(W, H) * 0.26;

 const colorIndex = Math.floor(tick / 100) % lineColors.length;
 const currentLineColor = lineColors[colorIndex];

 const bgRGB = hexToRGB("#020617");
 const tgtRGB = hexToRGB(currentLineColor);
 const mix = 0.12;
 const bgR = Math.floor(bgRGB.r * (1 - mix) + tgtRGB.r * mix);
 const bgG = Math.floor(bgRGB.g * (1 - mix) + tgtRGB.g * mix);
 const bgB = Math.floor(bgRGB.b * (1 - mix) + tgtRGB.b * mix);
 ctx.fillStyle = `rgba(${bgR},${bgG},${bgB},0.18)`;
 ctx.fillRect(0, 0, W, H);

 angXW += 0.0068;
 angYW += 0.0042;
 angZW += 0.0032;
 angXY += 0.0012;

 const pts3 = new Array(base.length);
 for (let i = 0; i < base.length; i++) {
 const p = base[i].slice();
 rot4(p, 0, 3, angXW);
 rot4(p, 1, 3, angYW);
 rot4(p, 2, 3, angZW);
 rot4(p, 0, 1, angXY);

 const wCam = 2.2;
 const wp = 1 / (wCam - p[3]);
 pts3[i] = [p[0] * wp, p[1] * wp, p[2] * wp, wp];
 }

 const faceIndex = Math.floor(tick / 180) % faces.length;
 const face = faces[faceIndex];
 const faceFill = lighten(currentLineColor, 0.35);

 ctx.fillStyle = faceFill;
 ctx.globalAlpha = 0.6;
 ctx.beginPath();
 for (let k = 0; k < face.length; k++) {
 const idx = face[k];
 const p = pts3[idx];
 const x = CX + p[0] * SCALE;
 const y = CY + p[1] * SCALE;
 if (k === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
 }
 ctx.closePath();
 ctx.fill();
 ctx.globalAlpha = 1;

 ctx.lineCap = "round";
 ctx.lineJoin = "round";
 for (let e = 0; e < edges.length; e++) {
 const [ia, ib] = edges[e];
 const a = pts3[ia];
 const b = pts3[ib];

 const ax = CX + a[0] * SCALE;
 const ay = CY + a[1] * SCALE;
 const bx = CX + b[0] * SCALE;
 const by = CY + b[1] * SCALE;

 const depth = (a[3] + b[3]) * 0.5;
 const alpha = Math.min(1, Math.max(0.22, depth * 1.1));
 const col = lineColors[e % lineColors.length];

 ctx.strokeStyle = col;
 ctx.globalAlpha = alpha;
 ctx.lineWidth = 1.05;
 ctx.beginPath();
 ctx.moveTo(ax, ay);
 ctx.lineTo(bx, by);
 ctx.stroke();
 ctx.globalAlpha = 1;
 }

 for (let i = 0; i < pts3.length; i++) {
 const p = pts3[i];
 const x = CX + p[0] * SCALE;
 const y = CY + p[1] * SCALE;
 const r = 2.5 * p[3] + 0.4;
 ctx.fillStyle = palette[5];
 ctx.beginPath();
 ctx.arc(x, y, r, 0, Math.PI * 2);
 ctx.fill();
 }
 }

 setInterval(draw, 30);
</script>