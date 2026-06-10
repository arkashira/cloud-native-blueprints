import typer
import yaml
from pathlib import Path
from axentx_blueprints.blueprint import Blueprint

app = typer.Typer()

@app.command()
def validate(file_path: str = typer.Argument(..., help="Path to the blueprint YAML file")):
    """Validates a blueprint against the Axentx schema."""
    try:
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        
        blueprint = Blueprint(**data)
        typer.echo(f"✅ Blueprint '{blueprint.name}' validated successfully.")
        typer.echo(f"   Version: {blueprint.version}")
        typer.echo(f"   Resources: {len(blueprint.resources)}")
    except yaml.YAMLError as e:
        typer.echo(f"❌ YAML Parse Error: {e}", err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.echo(f"❌ Validation Error: {e}", err=True)
        raise typer.Exit(code=1)

@app.command()
def list():
    """Lists available example blueprints."""
    blueprints_dir = Path("blueprints")
    if not blueprints_dir.exists():
        typer.echo("No blueprints directory found.")
        return
    
    for yaml_file in blueprints_dir.glob("*.yaml"):
        typer.echo(f"  - {yaml_file.name}")

if __name__ == "__main__":
    app()