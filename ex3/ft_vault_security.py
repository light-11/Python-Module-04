def secure_archive(name: str,
                   action: int,
                   content: str = "none") -> tuple[bool, str]:
    if action == 0:
        try:
            with open(name) as f:
                text = f.read()
            return (True, text)
        except Exception as e:
            return (False, str(e))
    else:
        try:
            with open(name, 'w') as f:
                f.write(content)
            return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))


def ft_vault_security() -> None:
    print("=== Cyber Archives - Vault Security ===")
    print(secure_archive("/not/existing/file", 0))
    print()
    print(secure_archive("/etc/shadow", 0))
    print()
    print(secure_archive("ancient_fragment.txt", 0))
    print()
    print(secure_archive("test.txt", 1, "Hello World"))


ft_vault_security()
