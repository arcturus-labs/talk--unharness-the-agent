---
name: building-software
description: Use this skill when creating or editing software in this workspace. Everything should be created and run in Rust unless the user explicitly asks otherwise.
---

# Building Software

In this workspace:

- everything should be created in Rust
- everything should be run with Rust tooling
- prefer `cargo` commands over ad hoc setup
- do not introduce another language unless the user explicitly asks for it
- whenever you create a program, explain exactly how to run it as a one-liner
- use absolute paths in run instructions

## Default project setup

For a new Rust CLI project:

```bash
cargo new my_app
cd my_app
cargo run
```

This creates a project like:

```text
my_app/
├── Cargo.toml
└── src/
    └── main.rs
```

For a library:

```bash
cargo new my_lib --lib
```

## Basic files

`Cargo.toml` defines the package and dependencies.

`src/main.rs` is the entry point for a binary app.

A very small program looks like this:

```rust
fn main() {
    println!("Hello, world!");
}
```

## How to install Rust

Use the official Rust installer: `rustup`.

Official docs:

- https://www.rust-lang.org/tools/install
- https://rustup.rs/
- https://doc.rust-lang.org/cargo/getting-started/installation.html

### macOS and Linux

Run:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Then open a new shell and verify:

```bash
rustc --version
cargo --version
```

### Windows

Download and run `rustup-init.exe` from:

- https://rustup.rs/

Then verify in a new terminal:

```powershell
rustc --version
cargo --version
```

## How to run programs

From a Rust project directory:

```bash
cargo run
```

To build without running:

```bash
cargo build
```

To build an optimized release binary:

```bash
cargo build --release
```

To run tests:

```bash
cargo test
```

To check code quickly without producing a final binary:

```bash
cargo check
```

## Working style

Prefer:

- `cargo new`
- `cargo run`
- `cargo check`
- `cargo test`
- `cargo build --release`

When adding code:

- keep the Rust project layout standard
- use clear, simple Rust
- prefer a small number of dependencies
- explain commands in terms of Cargo
- always include a one-line run command
- use an absolute-path example for that command
