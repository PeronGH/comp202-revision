# Cryptography

## Cryptography Basics
- Goal: Secure communication over insecure channels
- Message $M$ (plaintext) encrypted to ciphertext $C$, then decrypted back to $M$
- Symmetric encryption: Same key $K$ used for encryption and decryption
  - Examples: Substitution ciphers (e.g., Caesar cipher), one-time pad
  - Issues: Key distribution, keys can only be used once
- Public-key cryptography: Separate encryption key $E$ (public) and decryption key $D$ (private)
  - Properties: $D(E(M)) = M$, $E(D(M)) = M$, $E$ and $D$ easy to compute, infeasible to derive $D$ from $E$

## RSA Cryptosystem
- Based on difficulty of factoring large numbers 
- Key ideas from number theory:
  - Divisibility: $a \mid b$ if $b = ak$, some integer $k$ 
  - Prime numbers: only divisors are 1 and itself
  - Fundamental Theorem of Arithmetic: every integer $n > 1$ uniquely represented as product of primes
  - Greatest common divisor: $\gcd(a,b)$ = largest integer dividing both $a$ and $b$
  - If $d = \gcd(a,b)$, there exist integers $j,k$ with $d = ja + kb$ 
  - Modular arithmetic: $a \equiv b \pmod{n}$ if $a-b = kn$, some integer $k$

### Euclid's Algorithm

- Computes $\gcd(a,b)$ based on $\gcd(a,b) = \gcd(b, a \bmod b)$​
- Simplified steps:
  1. replace larger number with difference
  2. repeat step 1 until 2 numbers equal, and the result is GCD
- $O(\log(\max\{a,b\}))$ arithmetic operations
- (Optional) Extended version also finds integers $j,k$ with $d = ja+kb$​

### RSA Setup
- Primes $p,q$, modulus $n=pq$, $\phi(n) = (p-1)(q-1)$ 
- Public key: $(e,n)$ with $1 < e < \phi(n)$, $\gcd(e,\phi(n))=1$
- Private key: $d$ with $ed \equiv 1 \pmod{\phi(n)}$ 
- Encryption: $C = M^e \bmod n$
- Decryption: $M = C^d \bmod n$
- Correctness: $x^{ed} \equiv x \pmod{n}$ for $0 < x < n$

### Security and Efficiency
- Breaking RSA believed to require factoring $n = pq$
- Best known factoring algorithms are sub-exponential but super-polynomial
- Encryption, decryption, signing, verifying take $O(\log n)$ arithmetic operations using repeated squaring for modular exponentiation

### Digital Signatures
- Decrypt hash of message $M$ with private key to get signature $S$
- Anyone can verify $S$ by encrypting with public key and comparing to hash of $M$

## Summary

The key ideas are the basics of cryptography, the number theory behind RSA (primes, $\gcd$, modular arithmetic, Euclid's algorithm), the RSA operations, and the computational security based on hardness of factoring. Understanding the mathematical details is crucial for appreciating the design of RSA.
