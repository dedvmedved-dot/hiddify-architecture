# Diagrams

This directory contains architecture and network diagrams.

## Structure

```
diagrams/
  source/          - Diagram source files
  rendered/        - Rendered PNG/SVG/PDF files
```

## Source Formats

Supported diagram source formats:

- **Mermaid** (`.mmd`) — Markdown-embedded diagrams
- **PlantUML** (`.puml`) — UML diagrams
- **Graphviz** (`.dot`) — Graph diagrams
- **draw.io** (`.drawio`) — Visual diagrams

## Rendering

Diagrams are rendered automatically or manually:

```bash
# Render Mermaid diagram
mmdc -i diagrams/source/architecture.mmd -o diagrams/rendered/architecture.svg

# Render PlantUML
plantuml diagrams/source/sequence.puml
```

## Diagram Types

- System context diagrams
- Network topology diagrams
- Sequence diagrams
- Data flow diagrams
- Deployment diagrams
