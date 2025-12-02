# 🎁 OOPS Concepts — With Properties, Behaviours & Examples

## 🔹 1. Class
A **blueprint** or **template** to create objects.
It defines what an object *is* and *does*, but it is not the object itself.

**It defines:**
- **Properties (Attributes):** Variables that describe the object.
- **Behaviours (Methods):** Actions the object can perform.

### 📌 Example: Class Car
- **Properties:** `color`, `brand`, `speed`
- **Behaviours:** `start()`, `stop()`, `accelerate()`

> **Analogy:** A class is like an architect’s **blueprint**. It describes the building, but you can't live in the blueprint.

---

## 🔹 2. Object
An **actual instance** created from a class.
Every object has its **own copy** of properties but shares the behaviours defined in the class.

### 📌 Example
From the `Car` class, we create two objects:
- **Object 1:** Red BMW
- **Object 2:** Blue Audi

> Both share the same methods (`start()`, `stop()`), but their specific data (Color/Brand) is different.

---

## 🔹 3. Constructor
A **special method** that runs **automatically** when an object is created.
It is used to **initialize** (set) values for properties.

### 📌 Example
When you create a `Car` object, the constructor runs immediately to set defaults:
    brand = "BMW"
    color = "Black"
    speed = 0

> **Analogy:** Like the lights in a smart fridge turning on **automatically** the moment you open the door.

---

## 🔹 4. Polymorphism: Overloading vs Overriding

### A. Method Overloading (Compile-time)
- **Definition:** Same method name, **different** inputs (parameters).
- **Scope:** Happens within the **same class**.

**📌 Example:**
    drive()                // Just driving
    drive(speed)           // Driving at specific speed
    drive(speed, distance) // Driving specific speed for specific distance

*Same action, different ways to do it.*

### B. Method Overriding (Run-time)
- **Definition:** Child class **replaces** a method of the parent class.
- **Scope:** Happens between **Parent and Child classes**.

**📌 Example:**
- **Parent (Animal):** `sound()` → "Generic sound"
- **Child (Dog):** `sound()` → "Bark"
- **Child (Cat):** `sound()` → "Meow"

*Same method name, but the behavior changes based on the specific object.*

---

## 🔹 5. Object Relationships (Association, Aggregation, Composition)

| Type | Relationship | Dependency | Example |
| :--- | :--- | :--- | :--- |
| **Association** | "Just friends" | Independent | **Teacher ↔ Student**<br>(Teacher can exist without that specific student) |
| **Aggregation** | "Has-a" (Weak) | Separable | **School ↔ Teachers**<br>(If School closes, Teachers still exist) |
| **Composition** | "Has-a" (Strong) | Inseparable | **House ↔ Rooms**<br>(If House is destroyed, Rooms are gone too) |

---

# ⚡ Quick Summary

1. **Class** → Blueprint (Properties + Behaviours)
2. **Object** → Actual Instance (Uses the blueprint)
3. **Constructor** → Auto-starter (Initializes values)
4. **Overloading** → Same function, different inputs
5. **Overriding** → Same function, new logic in child
6. **Association** → Connected but independent
7. **Aggregation** → Separable ownership
8. **Composition** → Inseparable ownership (Life & Death connected)