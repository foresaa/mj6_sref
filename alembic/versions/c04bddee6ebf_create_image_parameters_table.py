"""Create image_parameters table

Revision ID: c04bddee6ebf
Revises: 
Create Date: 2024-09-17 18:29:14.064442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c04bddee6ebf'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image_parameters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('file_name', sa.String(), nullable=True),
    sa.Column('file_path', sa.String(), nullable=True),
    sa.Column('sref_number', sa.Integer(), nullable=True),
    sa.Column('sref_description', sa.String(), nullable=True),
    sa.Column('twitter_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_image_parameters_file_name'), 'image_parameters', ['file_name'], unique=False)
    op.create_index(op.f('ix_image_parameters_id'), 'image_parameters', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_image_parameters_id'), table_name='image_parameters')
    op.drop_index(op.f('ix_image_parameters_file_name'), table_name='image_parameters')
    op.drop_table('image_parameters')
    # ### end Alembic commands ###
