# Notes

### Handling new window popups

```python
base_window = driver.window_handles[0]
new_window = driver.window_handles[1]
driver.switch_to.window(new_window)
```

- When we use Facebook or other platforms to login we might get a new window pop up
- Inorder to access the new window we need to tell the driver to switch windows
- `driver.window_handles` - this lists all the windows open, new ones will be added at the end of lists