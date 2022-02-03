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
- [ ] Alert when laptop is unplugged.
- [x] Alert when laptop's lid is closed.
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


Note: You'll need to train your own ML model for maximum accuracy. Keep it under 1 mb for better performance and minimal cpu usage < 2% (M1 Processor)
The example model is 0.02 mb and works pretty well for me :D

```
Training Data:
     250: "intruder" pictures
     250: "person / empty" pictures
```
`Model size: 0.02 mb or 20 KB`
