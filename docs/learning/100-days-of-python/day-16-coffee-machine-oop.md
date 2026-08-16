# :material-language-python: Coffee Machine (OOP)

_Day 16 - the same coffee machine as [Day 15](day-15-coffee-machine.md), rebuilt with Object-Oriented Programming. Each responsibility becomes its own class: the menu, the coffee maker, and the money machine._{ .sj-lead }

!!! note "What's mine here"
    Angela provides the three classes (`Menu`, `CoffeeMaker`, `MoneyMachine`). The exercise is to **orchestrate** them - so `main.py` is the file I wrote: initialising the objects, running the machine loop, routing the `report` and `off` employee commands, and walking a drink through the find → resource check → payment → serve flow.

## main.py - running the machine

```python
--8<-- "docs/learning/100-days-of-python/code/day_016/main.py"
```

## Menu (provided)

```python
--8<-- "docs/learning/100-days-of-python/code/day_016/menu.py"
```

## Coffee maker (provided)

```python
--8<-- "docs/learning/100-days-of-python/code/day_016/coffee_maker.py"
```

## Money machine (provided)

```python
--8<-- "docs/learning/100-days-of-python/code/day_016/money_machine.py"
```
