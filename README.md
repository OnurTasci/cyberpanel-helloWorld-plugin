# 🌍 helloWorld - CyberPanel Plugin

The `helloWorld` plugin is a minimal example plugin for CyberPanel. It demonstrates how to integrate a custom plugin into the CyberPanel interface, including custom views and URL routing.

---

## ✨ Features

- Adds a custom URL route: `/helloWorld/`
- Returns a basic `Hello, World!` message
- Demonstrates plugin folder structure, Django views, and routing
- Lightweight and easy to extend

---

## 📁 Plugin Structure

```
helloWorld/
├── __init__.py
├── apps.py
├── urls.py
└── views.py
```

---

## 🚀 Installation

1. Upload the `helloWorld` folder **and** `helloWorld.zip` to the following directory on your server:

```
/usr/local/CyberCP/pluginInstaller
```

2. Connect to your server via SSH and run the following command:

```
cd /usr/local/CyberCP/pluginInstaller
python pluginInstaller.py install --pluginName helloWorld
```

3. Once installed, you should see the "Plugins > helloWorld" item in the CyberPanel sidebar. Clicking it will render your custom view.


```
https://your-server-ip:8090/helloWorld/
```


> Note: If any UI element does not appear immediately after installation, you can issue the remove command to remove it

## ❌ Remove

To remove the plugin, run the following command:

```
python pluginInstaller.py remove --pluginName helloWorld
```

---


## 🧪 Example View Output

Visiting the route will return:

```
Hello, World! from your CyberPanel plugin.
```

---

## 🤝 Contribution

This plugin is meant for learning and experimentation. Feel free to fork and build on it for your own CyberPanel projects!

@usmannasir

---

## 📄 License

MIT License

