# tickgen

**tickgen** is a lightweight Python utility that generates **strictly increasing numeric IDs** based on the current timestamp, including milliseconds precision.

Each ID is guaranteed to be greater than the previous one, making it ideal for:

- 🔐 Unique transaction identifiers  
- 🧾 Ordered event tracking  
- 🛠 Systems where database `AUTO_INCREMENT` is not viable

---

### 🧬 ID Structure

Each generated ID is composed of:

- **Last 2 digits of the year**
- **Last digit of the month**
- **Full day**
- **Hour**
- **Minute**
- **Second**
- **First two digits of milliseconds**

Example output:
2571200024080
2571200024082
etc.
