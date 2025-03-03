"""update external_data

Revision ID: f46b08eb03f7
Revises: 034e432ba480
Create Date: 2025-01-30 17:00:46.966730

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "f46b08eb03f7"
down_revision = "034e432ba480"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "external_supplier_data",
        sa.Column("event_sanctions", sa.String(), nullable=True),
    )
    op.add_column(
        "external_supplier_data",
        sa.Column("event_regulatory", sa.String(), nullable=True),
    )
    op.add_column(
        "external_supplier_data",
        sa.Column("event_bribery_fraud_corruption", sa.String(), nullable=True),
    )
    op.add_column(
        "external_supplier_data", sa.Column("event_pep", sa.String(), nullable=True)
    )
    op.add_column(
        "external_supplier_data",
        sa.Column("event_adverse_media_other_crimes", sa.String(), nullable=True),
    )
    op.add_column(
        "external_supplier_data",
        sa.Column("event_adverse_media_reputational_risk", sa.String(), nullable=True),
    )
    op.add_column(
        "external_supplier_data", sa.Column("legal", sa.String(), nullable=True)
    )
    op.add_column(
        "external_supplier_data", sa.Column("session_id", sa.String(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("external_supplier_data", "session_id")
    op.drop_column("external_supplier_data", "legal")
    op.drop_column("external_supplier_data", "event_adverse_media_reputational_risk")
    op.drop_column("external_supplier_data", "event_adverse_media_other_crimes")
    op.drop_column("external_supplier_data", "event_pep")
    op.drop_column("external_supplier_data", "event_bribery_fraud_corruption")
    op.drop_column("external_supplier_data", "event_regulatory")
    op.drop_column("external_supplier_data", "event_sanctions")
    # ### end Alembic commands ###
