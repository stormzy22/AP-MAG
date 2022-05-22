<img src="IMG/logo/AP-MAG-OFFiCiAL.png" alt="AP-MAG logo" style="display:block; margin:0 auto;"/>

<br/>
<br/>

# AP-MAG

### **Access Point Manager(AP-MAG)** is a **Linux based** network scanning tool that lets the user decide devices authorized to be on their network. The program also automatically kicks out (de-authenticate) devices not meant to be on the network.
---
---
<br/>
<h2><u>Installation</u></h2>

- git clone [https://github.com/stormzy22/AP-MAG](https://github.com/stormzy22/AP-MAG)
- cd AP-MAG
- pip install -r requirements.txt
- ./run


<p style="text-align:center;font-size:2.5rem;"><u>Usage</u></p>

---
1. ### input **scan** to discover connected devices on the wireless access point and it returns the number of devices connected.
![STEP 1](IMG/screenshots/s1.png "SCAN")

---
2. ### input **hosts** to view the list of connected devices.
![STEP 2](IMG/screenshots/s2.png "DISPLAY HOSTS")

---
3. ### input **save** to whitelist the current devices.
![STEP 3](IMG/screenshots/s3.png "SAVE HOSTS")

---
4. ### input **check** to validate the current devices connected to the access point.
![STEP 4](IMG/screenshots/s4.png "CHECK")

---
5. ### input **deauth** to deauthenticate invalid devices on the wireless access point.<br/> Close the terminal once the wireless access point have be identified.
![STEP 5](IMG/screenshots/s5.png "DEAUTH STEP 1")

---
6. ### Wait for 3sec then close the terminal.
![STEP 6](IMG/screenshots/s6.png "DEAUTH STEP 2")

---
7. ### Here's the final stage of deauthentication where all the invalid devices are kicked out.
![STEP 7](IMG/screenshots/s7.png "DEAUTH STEP 3")

---
8. ### Exiting and Cleaning up the program.
![STEP 7](IMG/screenshots/s8.png "EXITING THE PROGRAM")

---

<h2><u>Contributors</u></h2>

- [stormzy22](https://github.com/stormzy22)
- [Okon Divine](https://github.com/Okon-Divine)

