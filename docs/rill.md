<!-- markdownlint-disable -->

<a href="../rill/rill.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `rill`
rill 


---

<a href="../rill/rill.py#L109"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `inp`

```python
inp() → Stream
```

Entry point to construct a stream from an input. 


---

<a href="../rill/rill.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Stream`
The main class providing method chaining. 

<a href="../rill/rill.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(source: Callable[[], Iterable[str]])
```

Set source. 




---

<a href="../rill/rill.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `char_count`

```python
char_count() → Stream
```

WC-m-like line counting. 

---

<a href="../rill/rill.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_source`

```python
get_source() → Callable[[], Iterable[str]]
```

Return source for external access. 

---

<a href="../rill/rill.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `grep`

```python
grep(needle: str) → Stream
```

Grep functionality. 

---

<a href="../rill/rill.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `line_count`

```python
line_count() → Stream
```

WC-l-like line counting. 

---

<a href="../rill/rill.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `line_lengths`

```python
line_lengths() → Stream
```

Get the length of each line. 

---

<a href="../rill/rill.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `map_lines`

```python
map_lines(func: Callable[[str], str]) → Stream
```

Transform lines one by one. 

---

<a href="../rill/rill.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `replace`

```python
replace(frm: str, target: str) → Stream
```

SED-like text replacement. 

---

<a href="../rill/rill.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `show`

```python
show() → None
```

Print everything. 

---

<a href="../rill/rill.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `word_count`

```python
word_count() → Stream
```

WC-w-like line counting. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
