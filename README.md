# AP-MAG

### **Access Point Manager(AP-MAG)** is a **Linux based** network scanning tool that lets the user decide devices authorized to be on their network. The program also automatically kicks out (de-authenticate) devices not meant to be on the network.
---
---
<br/>
<h2><u>Installation</u></h2>

- git clone [https://github.com/stormzy22/AP-MAG](https://github.com/stormzy22/AP-MAG)
- cd AP-MAG

<h2><u>Usage</u></h2>

<table style="border: 3px solid; font-size:1.2rem">
<tr>
<td>scan</td>
<td>scans the local network, using the information from the primary network interface</td>
</tr>
<tr>
<td>hosts</td>
<td>display all the host discovered from the scan</td>
</tr>
<tr>
<td>save</td>
<td>creates a <b>whitelist</b> of devices that are meant to be on the network</td>
</tr>
<tr>
<td>check</td>
<td>compares the current devices on a network with the whitelist to give you the number of invalid devices on the network</td>
</tr>
<tr>
<td>deauth</td>
<td>
kicks out (de-auth) the invalid devices on the network
</td>
</tr>
<tr>
<td>quit / exit</td>
<td>cleans up / delete files created during the session <br/>
<u><b>NOTE:</b></u>&nbsp;this command doesn't delete the whitelist file
</td>
</tr>
<tr>
<td>quit -w / exit -w</td>
<td>cleans up / delete files created during the session and also delete the whitelist</td>
</tr>
</table>

---
---

<h2><u>Contributors</u></h2>

- [stormzy22](https://github.com/stormzy22)
- []()