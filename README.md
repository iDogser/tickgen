# tickgen

**tickgen** is a lightweight Python utility that generates **strictly increasing numeric IDs** based on the current timestamp, including milliseconds precision.
Each ID is guaranteed to be greater than the previous one*

---

### Limitations

The only potential risk of collision occurs when the generator is called **asynchronously and truly simultaneously** within the exact same **10-millisecond** window.
However, in real-world applications, due to natural delays introduced by:

- Network latency  
- Processing logic (validation, database, etc.)  
- Event loop scheduling  

the likelihood of two users triggering ID generation with **identical timing down to the tenth of a millisecond** is **extremely low**.
For most use cases – especially in web systems or event-driven backends – **tickgen** provides **practically collision-free identifiers** without requiring locks, mutexes, or centralized coordination.


---

### ID Structure

Each generated ID is composed of:

- **Last 2 digits of the year**
- **Full month**
- **Full day**
- **Hour**
- **Minute**
- **Second**
- **First two digits of milliseconds**

Example output: 25071202562170, 25071202562172, etc.
