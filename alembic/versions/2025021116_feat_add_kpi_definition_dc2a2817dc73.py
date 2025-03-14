"""feat : add kpi_definition

Revision ID: dc2a2817dc73
Revises: 3214c69bc32f
Create Date: 2025-02-11 10:16:24.368331

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "dc2a2817dc73"
down_revision = "3214c69bc32f"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ##
    op.add_column("cyes", sa.Column("kpi_definition", sa.String(), nullable=True))
    
    op.add_column("fstb", sa.Column("kpi_definition", sa.String(), nullable=True))
    
    op.add_column("lgrk", sa.Column("kpi_definition", sa.String(), nullable=True))
    
    op.add_column("news", sa.Column("kpi_definition", sa.String(), nullable=True))
    
    op.add_column("oval", sa.Column("kpi_definition", sa.String(), nullable=True))
    
    op.add_column("ovar", sa.Column("kpi_definition", sa.String(), nullable=True))
    
    op.add_column("rfct", sa.Column("kpi_definition", sa.String(), nullable=True))
    
    op.add_column("sape", sa.Column("kpi_definition", sa.String(), nullable=True))
    
    op.add_column("sown", sa.Column("kpi_definition", sa.String(), nullable=True))
    
    

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index("ix_users_table_user_id", "users_table", ["user_id"], unique=True)
    