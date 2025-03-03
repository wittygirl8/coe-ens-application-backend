"""feat : updation

Revision ID: 664700be9a80
Revises: 2ab49a10e528
Create Date: 2025-02-18 16:49:21.361933

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "664700be9a80"
down_revision = "2ab49a10e528"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    
    # Drop the existing primary key constraint on "id"
    op.drop_constraint('company_profile_pkey', 'company_profile', type_='primary')
    
    # Optionally, if needed, alter "id" column to allow nulls now that it's not a PK
    op.alter_column('company_profile', 'id',
                    existing_type=sa.INTEGER(),
                    nullable=True,
                    autoincrement=True)
    
    # Ensure that ens_id is NOT nullable so it can be the new primary key
    op.alter_column('company_profile', 'ens_id',
                    existing_type=sa.VARCHAR(length=255),
                    nullable=False)
    
    # Create a new primary key constraint on the "ens_id" column
    op.create_primary_key('company_profile_pkey', 'company_profile', ['ens_id'])
def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass