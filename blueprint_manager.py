class BlueprintManager:
    def __init__(self):
        self.blueprints = []

    def create_blueprint(self, name, description, role_required):
        if role_required not in self.get_user_roles():
            return f"Error: User does not have the required role '{role_required}' to create a blueprint."
        
        blueprint = {
            'name': name,
            'description': description
        }
        self.blueprints.append(blueprint)
        return f"Blueprint '{name}' created successfully."

    def list_blueprints(self):
        if not self.blueprints:
            return "No blueprints available."
        return "\n".join([f"{bp['name']}: {bp['description']}" for bp in self.blueprints])

    def get_user_roles(self):
        # This method should return a list of roles for the current user.
        # For demonstration purposes, we'll assume the user has the 'admin' role.
        return ['admin']

# Example usage
if __name__ == "__main__":
    manager = BlueprintManager()
    print(manager.create_blueprint("WebApp", "A simple web application blueprint", "admin"))
    print(manager.list_blueprints())