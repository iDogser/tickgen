# tickgen

**tickgen** is a lightweight Python utility that generates **strictly increasing numeric IDs** based on the current timestamp, including millisecond precision.  
Each ID is guaranteed to be greater than the previous one.

---

### Limitations

The only potential risk of collision occurs when the generator is called **asynchronously and truly simultaneously** within the exact same **10-millisecond** window.

However, in real-world applications, due to natural delays introduced by:
- Network latency  
- Processing logic  
- Event loop scheduling  

the likelihood of two users triggering ID generation with **identical timing down to the tenth of a millisecond** is **extremely low**.
For most use cases – especially in web systems or event-driven backends – **tickgen** provides **practically collision-free identifiers**.

---

### ID Structure

Each generated ID is composed of:

- **Last digit of the year**  
- **Full month**  
- **Full day**  
- **Hour**  
- **Minute**  
- **Second**  
- **First two digits of milliseconds**

Example output:
5071211264210
5071211264211
5071211264213
5071211264215
5071211264216

---

### Note

If you use the **last 1 digit of the year**, the system will provide unique identifiers for **10 years**.  
If you use the **last 2 digits of the year**, the system will safely cover a **100-year timespan**.
