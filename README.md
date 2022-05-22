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
2. ### input **hosts** to view the list of connected devices
![STEP 2](IMG/screenshots/s2.png "DISPLAY HOSTS")

---
3. ### input **save** to whitelist the current devices
![STEP 3](IMG/screenshots/s3.png "SAVE HOSTS")

---
4. ### input **check** to validate the current devices connected to the access point.
![STEP 4](IMG/screenshots/s4.png "CHECK")

---
![STEP 5](IMG/screenshots/s5.png "DEAUTH STEP 1")

---
![STEP 6](IMG/screenshots/s6.png "DEAUTH STEP 2")

---
![STEP 7](IMG/screenshots/s7.png "DEAUTH STEP 3")

---
![STEP 7](IMG/screenshots/s8.png "EXITING THE PROGRAM")

---

<h2><u>Contributors</u></h2>

- [stormzy22](https://github.com/stormzy22)
- [Okon Divine](https://github.com/Okon-Divine)

<!-- msg = """
    STEP 1:\b
    \tinput [bold green]scan[/bold green] to discover connected devices on your network\b
    STEP 2:\b
    \tinput [bold green]hosts[/bold green] to view connected devices\b
    STEP 3:\b
    \tinput [bold green]save[/bold green] to whitelist the current devices\b
    STEP 4:\b
    \tinput [bold green]check[/bold green] to validate the current devices connected to the access point.
    \t[yellow bold]NOTE:[/yellow bold] The [bold green]check[/bold green] command compares the current devices connected to the access point
    \twith the whitelist then filters the devices that aren't in the whitelist and save them in the blacklist\b
    STEP 5:\b
    \tinput [bold green]deauth[/bold green] to deauthenticate invalid devices\b
    STEP 6:\b
    \tinput [bold green]exit / quit[/bold green] to exit the program and clean files created during the session excluding the whitelist
    STEP 7:\b
    \tinput [bold green]exit -w / quit -w [/bold green] to exit the program and clean files created during the session including the whitelist

""" -->