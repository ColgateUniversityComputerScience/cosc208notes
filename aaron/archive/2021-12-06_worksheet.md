# Networking: Addressing(continued); Routing
_COSC 208, Introduction to Computer Systems, 2021-12-06_

## Announcements
* Project 3 due tomorrow at 11pm
* 2nd DEI reflection due tomorrow at 11pm
* Attend faculty candidate research talks
    * 11:20am tomorrow and Wed, Dec 15
    * Earn 2 points of extra credit on final exam for each talk you attend (earnings capped at 4 points)

## Outline
* Internet Protocol (IP) addresses
* Subnetting
* Routing unplugged

## No-warmup: Happy Monday!

<div style="page-break-after:always;"></div>

## Routing unplugged
During this activity, each person will play the role of a network router. You will be “connected” to one or more neighboring routers (i.e., group members). In total, the network will have 5 or 6 routers. 

Your goal is to be able to forward packets from one router to another until a packet reaches its intended destination. A packet will be represented by a piece of paper, which includes: 
* the source router’s name
* the destination router’s name
* a secret message

For example: 
```
Src = Vint, Dst = Radia, Secret = Go 'gate!
```

In your group, you may use your **voice** to talk with your group members about:
* The instructions for the activity
* Ideas for how to solve the problem
* How well your approach worked

You must use **notes** (written on pieces of paper) to:
* Send a packet to another router
* Share the names of your neighboring routers or the contents of packets you have received
* Share information you learned from neighboring routers

You may only pass notes to your neighboring routers. You may not pass a note to a router who is not your neighbor.

Now complete the following steps:
1. Discuss (with your voices) how each router should behave to ensure packets reach their destination. During the discussion, **do not share any information that can only be shared by passing notes** (see the list above).
2. Everyone should behave as you agreed upon. You should only use your voice to clarify the instructions and how you should behave. **All other information must be shared by passing notes to neighboring routers.**
3. When the group is ready to forward packets (you can use your voices to check if everyone is ready), the person whose first name comes first in the alphabet should create a packet with:
    1. Their name as the source 
    2. A destination router (i.e., person) of their choosing — choose a router that is part of your group, but is not one of your neighbors
    3. A secret message of their choosing

    **The packet and all other information must be sent by passing notes to neighboring routers.** You should only use your voice to clarify the instructions and how you should behave.

    The destination router should verbally announce when they receive the packet.

4. Discuss (with your voices) whether your approach worked. If not, what went wrong? How would you change your behavior?
5. If time allows, try your modified approach.

```
R1 --- R4 --- R6
|      |      |
R5 --- R2 --- R3
 \____________/
```

<div style="page-break-after:always;"></div>

You are Router 1.

Your neighbors are Router 4 and Router 5.

---

You are Router 2.

Your neighbors are Router 3, Router 4, and Router 5.

---

You are Router 3.

Your neighbors are Router 2, Router 5, and Router 6.

---

You are Router 4.

Your neighbors are Router 1, Router 2, and Router 6.

---

You are Router 5.

Your neighbors are Router 1, Router 2, and Router 3.

---

You are Router 6. 

Your neighbors are Router 3 and Router 4.

<div style="page-break-after:always;"></div>

# Router 1

---

# Router 2

---

# Router 3

---

# Router 4

---

# Router 5

---

# Router 6