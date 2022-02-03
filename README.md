# bigbrother
### Ai Accelerated Laptop Watcher Thingy
<div align="center">
<img src="https://user-images.githubusercontent.com/43297314/152235522-163b2f4e-1ac4-4428-a3b8-29feb28ba55c.png" width="200px">
</div>

So How does it work?
> Uses Apple's Beautiful CoreML tool and Python's amazing Open-CV to see if your precious laptop gets picked up or tampered with when you're out and about...peeing

Then
> Notifies by either sending a message / images though discord webhook or screams at the intruder. 
> 
> Saves the last x seconds of video footage before and after tampering and sends it to you if you want.



*Could be useful in school library or something? :)*

----

WIP

- [x] Custom FPS
- [x] Custom Buffer limit (Seconds to record before and after incident
- [x] Readable Codebase
- [x] Video DEBUG view
- [x] Created a Machine learning model
- [x] Analyzing every X frames using the model
- [ ] Discord webhook intergration
- [ ] Display, QR code + Laptop is protected + Do not come close or something scary +  webcam footage and data points window (full screen)
- [ ] Password integration to lock and unlock the device
- [ ] Ctrl + C protection *run in bg using nohup*
- [ ] Specific Key Protection: Only deactivates if someone presses a specific key within 3 seconds.
- [ ] Ability to RICK ROLL the intruder if tampering occurs.
