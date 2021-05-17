class Node:
    def __init__(self):
        self.val = ""
        self.children = []


class Problem:
    """
    Print N-ary Tree

    @FakeMesa ~/P/A/mola (master)> tree
    .
    ├── README.md
    ├── charts
    │   └── mola
    │       ├── Chart.yaml
    │       ├── README.md
    │       ├── templates
    │       │   ├── autoscaling.yaml
    │       │   ├── deployment.yaml
    │       │   ├── nginx-config.yaml
    │       │   ├── scheduledscaling.yaml
    │       │   ├── service.yaml
    │       │   ├── serviceaccount.yaml
    │       │   └── sigsci-config.yaml
    │       └── values.yaml
    ├── cw-fill-query.json
    ├── pipelines
    │   ├── auto-multi-deploy.pp
    │   ├── delete-resources.pp
    │   └── simple-deploy.pp
    └── values
        ├── aor.yaml
        ├── ava.yaml
        ├── base_values.yaml
        └── target_environment_values.yaml
    """

    def mNode(self, val, children):
        n = Node()
        n.val = val
        n.children = children
        return n

    def traverse(self, root, depth):
        if depth == 0:
            print(root.val)
        else:
            temp = "|   " * depth + "──" + "  " + root.val
            print(temp)

        for child in root.children:
            self.traverse(child, depth + 1)


if __name__ == "__main__":
    sol = Problem()

    r = sol.mNode("root", [
        sol.mNode("folder1", [
            sol.mNode("folder11", [
                sol.mNode("file1", [])
            ]),
            sol.mNode("file2", []),
        ]),
        sol.mNode("file3", []),
        sol.mNode("folder2", [
            sol.mNode("file4", [])
        ])
    ])

    sol.traverse(r, 0)
